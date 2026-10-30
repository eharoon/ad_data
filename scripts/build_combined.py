#!/usr/bin/env python3
"""Merge the AD source files into one table keyed by participant and timepoint.

All linking decisions (how each file's raw ID maps to a canonical participant
ID, which timepoint each row belongs to, and any variable renames) live in
config/sources.yaml. A source whose ID or timepoint rule is still "TODO" is
skipped and listed in the QC report, so the script never guesses a rule.

Outputs:
  <out-dir>/<table>.csv           one merged table per `table` in the config
                                  (default "combined"; git-ignored, holds data)
  docs/data_dictionary.csv        one row per variable: source file, sheet,
                                  original column, rename
  docs/merge_qc_report.md         per-source counts, unmatched IDs, duplicate
                                  keys, conflicting values, skipped sources

Usage:
  python scripts/build_combined.py --data-dir /path/to/01_Comb_folder
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import yaml

REPO = Path(__file__).resolve().parent.parent
PID, TP = "participant_id", "timepoint"
TODO = "TODO"
DEFAULT_TABLE = "combined"


# ---------------------------------------------------------------- config ---

def load_config(path: Path) -> dict:
    with open(path) as fh:
        cfg = yaml.safe_load(fh)
    cfg.setdefault("sources", [])
    cfg.setdefault("id_format", TODO)
    cfg.setdefault("roster", None)
    return cfg


def unresolved(src: dict, cfg: dict) -> list[str]:
    """Return the rules a source still needs before it can be merged."""
    missing = []
    if src.get("id_format", cfg.get("id_format")) in (None, TODO):
        missing.append("id_format")
    if src.get("id_rule") in (None, TODO):
        missing.append("id_rule")
    if src.get("timepoint") in (None, TODO):
        missing.append("timepoint")
    return missing


# ------------------------------------------------------------- reading ---

def read_source(src: dict, data_dir: Path) -> pd.DataFrame:
    path = data_dir / src["file"]
    header = src.get("header_row", 0)
    if path.suffix.lower() in (".xlsx", ".xls"):
        df = pd.read_excel(path, sheet_name=src.get("sheet", 0), header=header, dtype=object)
    else:
        df = pd.read_csv(path, header=header, dtype=object)
    # Excel sheets often carry blank trailing columns and rows.
    df = df.loc[:, [not str(c).startswith("Unnamed:") for c in df.columns]]
    df = df.dropna(how="all")
    df.columns = [str(c).strip() for c in df.columns]
    return df


def canonical_id(raw, rule: dict, id_format: str, crosswalk: dict | None):
    """Map one raw ID to the canonical participant ID, or None if it fails."""
    if raw is None or (isinstance(raw, float) and pd.isna(raw)):
        return None
    text = str(raw).strip()
    if text.endswith(".0"):  # numeric IDs read from Excel
        text = text[:-2]
    kind = rule["type"]
    if kind == "crosswalk":
        text = crosswalk.get(text) if crosswalk else None
        if text is None:
            return None
    elif kind == "regex":
        m = re.fullmatch(rule["pattern"], text)
        if not m:
            return None
        text = m.group(rule.get("group", 1))
    elif kind != "as_is":
        raise ValueError(f"unknown id_rule type: {kind}")
    try:
        return id_format.format(int(text))
    except ValueError:
        return id_format.format(text) if "{}" in id_format else None


def load_crosswalk(rule: dict, data_dir: Path) -> dict | None:
    if rule.get("type") != "crosswalk":
        return None
    cw = read_source({"file": rule["file"], "sheet": rule.get("sheet", 0)}, data_dir)
    return {
        str(k).strip().removesuffix(".0"): str(v).strip().removesuffix(".0")
        for k, v in zip(cw[rule["from"]], cw[rule["to"]])
        if pd.notna(k) and pd.notna(v)
    }


def assign_timepoint(df: pd.DataFrame, rule) -> pd.Series:
    if isinstance(rule, str):
        return pd.Series(rule, index=df.index)
    col = df[rule["column"]].astype(str).str.strip()
    mapping = rule.get("map")
    return col.map(mapping) if mapping else col


# ------------------------------------------------------------- merging ---

@dataclass
class SourceResult:
    name: str
    status: str
    rows_read: int = 0
    rows_kept: int = 0
    unparsed_ids: list = field(default_factory=list)
    unmapped_timepoints: list = field(default_factory=list)
    duplicate_keys: list = field(default_factory=list)
    ids: set = field(default_factory=set)
    note: str = ""


def prepare(src: dict, cfg: dict, data_dir: Path):
    """Read one source and return (frame keyed by PID/TP, dictionary rows, result)."""
    res = SourceResult(src["name"], "merged")
    df = read_source(src, data_dir)
    res.rows_read = len(df)

    crosswalk = load_crosswalk(src["id_rule"], data_dir)
    ids = df[src["id_column"]].map(lambda v: canonical_id(v, src["id_rule"], src.get("id_format", cfg["id_format"]), crosswalk))
    res.unparsed_ids = sorted({str(r) for r, i in zip(df[src["id_column"]], ids) if pd.isna(i) and pd.notna(r)})
    tps = assign_timepoint(df, src["timepoint"])
    if isinstance(src["timepoint"], dict):
        res.unmapped_timepoints = sorted(set(df.loc[tps.isna(), src["timepoint"]["column"]].astype(str)))

    key_cols = {src["id_column"]}
    if isinstance(src["timepoint"], dict):
        key_cols.add(src["timepoint"]["column"])
    drop = set(src.get("drop_columns", [])) | key_cols
    rename = src.get("rename", {}) or {}
    prefix = src.get("prefix", "") or ""

    values = df[[c for c in df.columns if c not in drop]].copy()
    transforms = {}
    for c, mapping in (src.get("recode") or {}).items():
        lookup = {str(k): v for k, v in mapping.items()}
        values[c] = values[c].map(lambda v: lookup.get(str(v).removesuffix(".0"), v) if pd.notna(v) else v)
        transforms[c] = "recoded " + ", ".join(f"{k}->{v}" for k, v in mapping.items())
    for c, factor in (src.get("scale") or {}).items():
        values[c] = pd.to_numeric(values[c], errors="coerce") * factor
        transforms[c] = f"multiplied by {factor}"
    dict_rows = []
    new_cols = []
    for c in values.columns:
        new = rename.get(c, prefix + c)
        new_cols.append(new)
        dict_rows.append({
            "variable": new,
            "source": src["name"],
            "file": src["file"],
            "sheet": src.get("sheet", ""),
            "original_column": c,
            "renamed": new != c,
            "rename_reason": "explicit rename" if c in rename else ("prefix" if prefix else ""),
            "transform": transforms.get(c, ""),
        })
    values.columns = new_cols
    values.insert(0, TP, tps.values)
    values.insert(0, PID, ids.values)
    values = values.dropna(subset=[PID, TP])

    dup_mask = values.duplicated([PID, TP], keep=False)
    if dup_mask.any():
        res.duplicate_keys = sorted(map(tuple, values.loc[dup_mask, [PID, TP]].drop_duplicates().values))
        if src.get("on_duplicate", "error") == "first":
            values = values.drop_duplicates([PID, TP], keep="first")
            res.note = "duplicate keys found; kept first row per key (on_duplicate: first)"
        else:
            res.status = "skipped"
            res.note = "duplicate participant/timepoint keys; set on_duplicate or fix the source"
            return None, dict_rows, res

    res.rows_kept = len(values)
    res.ids = set(values[PID])
    return values.set_index([PID, TP]), dict_rows, res


def merge_all(cfg: dict, data_dir: Path, sources: list[dict]):
    combined = None
    dictionary, results, conflicts = [], [], []
    owner = {}  # output column -> source that supplied it first

    for src in sources:
        if not src.get("include", True):
            results.append(SourceResult(src["name"], "excluded", note=src.get("exclude_reason", "include: false")))
            continue
        missing = unresolved(src, cfg)
        if missing:
            results.append(SourceResult(src["name"], "awaiting rules", note="needs " + ", ".join(missing)))
            continue
        frame, dict_rows, res = prepare(src, cfg, data_dir)
        results.append(res)
        if frame is None:
            continue
        dictionary.extend(dict_rows)
        if combined is None:
            combined = frame
            owner.update({c: src["name"] for c in frame.columns})
            continue
        overlap = [c for c in frame.columns if c in combined.columns]
        for c in overlap:
            both = combined[[c]].join(frame[[c]], how="inner", lsuffix="_a", rsuffix="_b").dropna()
            differ = both[both[f"{c}_a"].astype(str) != both[f"{c}_b"].astype(str)]
            for (pid, tp), row in differ.iterrows():
                conflicts.append({
                    "table": src.get("table", DEFAULT_TABLE), PID: pid, TP: tp, "variable": c,
                    "kept_source": owner[c], "kept_value": row[f"{c}_a"],
                    "other_source": src["name"], "other_value": row[f"{c}_b"],
                })
        combined = combined.reindex(combined.index.union(frame.index))
        for c in overlap:
            # Earlier source wins where both have a value; the later one fills gaps.
            combined[c] = combined[c].combine_first(frame[c].reindex(combined.index))
        rest = frame.drop(columns=overlap)
        combined = combined.join(rest, how="left")
        owner.update({c: src["name"] for c in rest.columns})

    if combined is not None:
        combined = combined.sort_index().reset_index()
    return combined, dictionary, results, conflicts


# ------------------------------------------------------------- reports ---

def fmt_list(items, limit=40) -> str:
    items = [", ".join(map(str, i)) if isinstance(i, tuple) else str(i) for i in items]
    if not items:
        return "none"
    shown = "; ".join(items[:limit])
    return shown + (f"; … ({len(items) - limit} more)" if len(items) > limit else "")


def roster_for(cfg: dict, table: str):
    """`roster` is one source name, or a {table: source name} mapping."""
    roster = cfg.get("roster")
    return roster.get(table) if isinstance(roster, dict) else roster


def write_qc(path: Path, cfg, tables: dict, results, conflicts, dictionary):
    lines = [
        "# Merge QC report",
        "",
        f"Generated {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC} by `scripts/build_combined.py`.",
        "",
        "## Summary",
        "",
    ]
    if not tables:
        lines.append("No source was merged, because every source is still waiting for confirmed linking rules or is excluded.")
    for table, (combined, tresults) in tables.items():
        lines.append(
            f"- `{table}.csv`: {len(combined)} participant-timepoint rows, "
            f"{combined[PID].nunique()} participants and {combined.shape[1] - 2} variables "
            f"from {sum(r.status == 'merged' for r in tresults)} sources."
        )
    merged = [r for r in results if r.status == "merged"]
    lines += ["", "## Sources", "", "| Source | Status | Rows read | Rows kept | Participants | Note |", "|---|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r.name} | {r.status} | {r.rows_read or ''} | {r.rows_kept or ''} | {len(r.ids) or ''} | {r.note} |")

    lines += ["", "## IDs that could not be mapped", ""]
    lines += [f"- **{r.name}**: {fmt_list(r.unparsed_ids)}" for r in merged if r.unparsed_ids] or ["None."]
    lines += ["", "## Timepoint values with no mapping", ""]
    lines += [f"- **{r.name}**: {fmt_list(r.unmapped_timepoints)}" for r in merged if r.unmapped_timepoints] or ["None."]

    lines += ["", "## Unmatched participants", ""]
    if not tables:
        lines.append("Not checked, because nothing was merged.")
    for table, (_, tresults) in tables.items():
        roster_name = roster_for(cfg, table)
        roster = next((r.ids for r in tresults if r.name == roster_name and r.status == "merged"), None)
        if roster is None:
            lines.append(f"`{table}`: no roster source is set (`roster` in config/sources.yaml), so unmatched IDs are not checked.")
            continue
        lines.append(f"`{table}`, checked against the roster source `{roster_name}` ({len(roster)} participants):")
        lines.append("")
        for r in tresults:
            if r.name == roster_name or r.status != "merged":
                continue
            extra, absent = sorted(r.ids - roster), sorted(roster - r.ids)
            lines.append(f"- **{r.name}**: {len(extra)} not in roster ({fmt_list(extra)}); {len(absent)} roster participants missing ({fmt_list(absent)}).")

    lines += ["", "## Duplicate participant-timepoint keys", ""]
    lines += [f"- **{r.name}**: {fmt_list(r.duplicate_keys)}" for r in results if r.duplicate_keys] or ["None."]

    lines += ["", "## Conflicting values", ""]
    if not conflicts:
        lines.append("None. No variable was supplied by more than one source with different values.")
    else:
        lines.append(f"{len(conflicts)} cells differ between sources. The earlier source in the config was kept.")
        lines += ["", f"| table | {PID} | {TP} | variable | kept source | kept | other source | other |", "|---|---|---|---|---|---|---|---|"]
        for c in conflicts[:200]:
            lines.append(f"| {c['table']} | {c[PID]} | {c[TP]} | {c['variable']} | {c['kept_source']} | {c['kept_value']} | {c['other_source']} | {c['other_value']} |")
        if len(conflicts) > 200:
            lines.append(f"\n{len(conflicts) - 200} more conflicts are in the output folder's conflicts.csv.")

    dupe_vars = pd.Series([d["variable"] for d in dictionary]).value_counts()
    shared = dupe_vars[dupe_vars > 1]
    lines += ["", "## Variables supplied by more than one source", ""]
    lines.append(fmt_list(list(shared.index)) if len(shared) else "None.")
    path.write_text("\n".join(lines) + "\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", type=Path, default=REPO / "config" / "sources.yaml")
    ap.add_argument("--data-dir", type=Path, help="folder holding the raw source files (overrides config data_dir)")
    ap.add_argument("--out-dir", type=Path, default=REPO / "output")
    ap.add_argument("--docs-dir", type=Path, default=REPO / "docs")
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    data_dir = args.data_dir or (args.config.parent / cfg.get("data_dir", ".")).resolve()
    if not data_dir.is_dir():
        sys.exit(f"data folder not found: {data_dir}")

    # Sources with a different `table` (e.g. a second cohort) go to their own output table.
    groups: dict[str, list] = {}
    for src in cfg["sources"]:
        groups.setdefault(src.get("table", DEFAULT_TABLE), []).append(src)
    tables, dictionary, results, conflicts = {}, [], [], []
    for table, sources in groups.items():
        combined, d, r, c = merge_all(cfg, data_dir, sources)
        dictionary += [{"table": table, **row} for row in d]
        results += r
        conflicts += c
        if combined is not None:
            tables[table] = (combined, r)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    args.docs_dir.mkdir(parents=True, exist_ok=True)
    for table, (combined, _) in tables.items():
        combined.to_csv(args.out_dir / f"{table}.csv", index=False)
    pd.DataFrame(conflicts, columns=["table", PID, TP, "variable", "kept_source", "kept_value", "other_source", "other_value"]).to_csv(
        args.out_dir / "conflicts.csv", index=False)
    pd.DataFrame(dictionary, columns=["table", "variable", "source", "file", "sheet", "original_column", "renamed", "rename_reason", "transform"]).to_csv(
        args.docs_dir / "data_dictionary.csv", index=False)
    write_qc(args.docs_dir / "merge_qc_report.md", cfg, tables, results, conflicts, dictionary)

    for r in results:
        print(f"{r.status:15} {r.name}  {r.note}")
    print(f"QC report: {args.docs_dir / 'merge_qc_report.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
