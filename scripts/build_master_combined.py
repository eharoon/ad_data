#!/usr/bin/env python3
"""Build the combined master from dat_harmonized.csv plus Midlife albumin.

dat_harmonized.csv (!ADgrant/R/ADMs, written by harmonize_data.qmd) is the
single master and provenance file. This script never edits it. It adds the
Midlife (discovery) plasma albumin, CSF albumin and albumin quotient (QAlb)
from QAlbumin_discovery_values_2026-11-12.csv (owner-final 2026-11-12) to the
Mlife rows, the same way qalb_adjustment_2026-11-12.qmd does, and writes the
result as a second master, dat_combined.csv, with a provenance note beside it.

Phenom rows already carry plasma albumin, CSF albumin and QAlb in the master
and are left exactly as they are.

Usage:
  python scripts/build_master_combined.py \\
      --master  ".../R/ADMs/dat_harmonized.csv" \\
      --qalb    ".../!writing plan/Tables/QAlbumin_discovery_values_2026-11-12.csv" \\
      --out-dir ".../R/ADMs"
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

# SHA-256 of the master as confirmed on 2026-11-20. If the master changes,
# the script stops so the change is noticed rather than silently absorbed.
MASTER_SHA256 = "05ebb763cd8ad287655ceeb481e3b1df92cd58c12bfb8d1e29f87e00c91e8388"

# master column <- discovery-file column
ALBUMIN = {
    "plasma_albumin_gdl": "plasma_alb_mean_gdl",
    "csf_albumin_gdl": "csf_alb_mean_gdl",
    "qalbumin": "qalb_x1000",
}
EXPECTED_MATCHES = 54  # Midlife participants with CSF


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(master_path: Path, qalb_path: Path, allow_new_master: bool = False):
    digest = sha256(master_path)
    if digest != MASTER_SHA256 and not allow_new_master:
        sys.exit(
            f"{master_path.name} has changed since it was confirmed as the master "
            f"(sha256 {digest[:12]}..., expected {MASTER_SHA256[:12]}...). "
            "Confirm the new version, then rerun with --allow-new-master."
        )
    master = pd.read_csv(master_path)
    disc = pd.read_csv(qalb_path)

    missing = [c for c in ["id", "age", "subgrp", *ALBUMIN.values()] if c not in disc.columns]
    if missing:
        sys.exit(f"{qalb_path.name} lacks columns: {missing}")
    if disc["id"].duplicated().any():
        sys.exit(f"{qalb_path.name} has duplicate ids: {sorted(disc.loc[disc['id'].duplicated(), 'id'])}")

    mlife = master["study"] == "Mlife"
    already = master.loc[mlife, list(ALBUMIN)].notna().any(axis=None)
    if already:
        sys.exit("The master already holds Mlife albumin values; refusing to overwrite them.")

    # Same identity checks as qalb_adjustment_2026-11-12.qmd: every discovery
    # row must match a Mlife participant on age (within 0.6 y) and group.
    chk = master.loc[mlife, ["id", "age", "subgrp"]].merge(
        disc[["id", "age", "subgrp"]], on="id", suffixes=("", "_lab"))
    problems = []
    if len(chk) != EXPECTED_MATCHES:
        problems.append(f"{len(chk)} Mlife ids matched, expected {EXPECTED_MATCHES}")
    unmatched = sorted(set(disc["id"]) - set(master.loc[mlife, "id"]))
    if unmatched:
        problems.append(f"discovery ids not among Mlife rows: {unmatched}")
    bad_age = chk.loc[(chk["age"] - chk["age_lab"]).abs() >= 0.6, "id"].tolist()
    if bad_age:
        problems.append(f"age disagrees by >= 0.6 y for ids {bad_age}")
    bad_grp = chk.loc[chk["subgrp"] != chk["subgrp_lab"], "id"].tolist()
    if bad_grp:
        problems.append(f"group disagrees for ids {bad_grp}")
    if problems:
        sys.exit("Identity checks failed: " + "; ".join(problems))

    combined = master.copy()
    lookup = disc.set_index("id")
    for col, src in ALBUMIN.items():
        combined.loc[mlife, col] = combined.loc[mlife, "id"].map(lookup[src]).values

    # QAlb should equal CSF / plasma albumin x 1000 in both cohorts.
    ratio = combined["csf_albumin_gdl"] / combined["plasma_albumin_gdl"] * 1000
    has = combined["qalbumin"].notna() & ratio.notna()
    off = combined.loc[has & ~np.isclose(combined["qalbumin"], ratio, rtol=1e-3), ["study", "id"]]

    # Every non-albumin cell must be identical to the master.
    others = [c for c in master.columns if c not in ALBUMIN]
    assert combined[others].equals(master[others])
    assert combined.loc[~mlife, list(ALBUMIN)].equals(master.loc[~mlife, list(ALBUMIN)])

    info = {
        "master_sha256": digest,
        "qalb_sha256": sha256(qalb_path),
        "n_rows": len(combined),
        "filled": {c: int(combined.loc[mlife, c].notna().sum()) for c in ALBUMIN},
        "qalb_ratio_mismatch": off.values.tolist(),
    }
    return combined, info


def write_provenance(path: Path, master_path: Path, qalb_path: Path, info: dict):
    filled = "\n".join(f"| `{c}` | `{s}` | {info['filled'][c]} |" for c, s in ALBUMIN.items())
    mismatch = (
        "QAlb equals CSF albumin / plasma albumin x 1000 for every participant with all three values."
        if not info["qalb_ratio_mismatch"]
        else f"QAlb differs from CSF / plasma albumin x 1000 for: {info['qalb_ratio_mismatch']}."
    )
    path.write_text(f"""# dat_combined.csv provenance

Built {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC} by `scripts/build_master_combined.py` (eharoon/ad_data).

## Sources

| Role | File | SHA-256 |
|---|---|---|
| Master (unchanged) | `{master_path.name}` | `{info['master_sha256']}` |
| Midlife albumin | `{qalb_path.name}` | `{info['qalb_sha256']}` |

## What was added

`dat_combined.csv` is `dat_harmonized.csv` with Midlife (study = Mlife) albumin filled in. All other cells are identical to the master. Phenom albumin values come from the master unchanged.

| Column | Taken from | Mlife participants filled |
|---|---|---|
{filled}

Rows are matched on `id` within study = Mlife. Every Midlife albumin row was checked to agree with the master on age (within 0.6 years) and group before merging.

{mismatch}

Rows: {info['n_rows']}.
""")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--master", type=Path, required=True)
    ap.add_argument("--qalb", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--allow-new-master", action="store_true")
    args = ap.parse_args(argv)

    combined, info = build(args.master, args.qalb, args.allow_new_master)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    combined.to_csv(args.out_dir / "dat_combined.csv", index=False)
    write_provenance(args.out_dir / "dat_combined_provenance.md", args.master, args.qalb, info)
    print(f"dat_combined.csv: {info['n_rows']} rows; Mlife filled {info['filled']}")
    if info["qalb_ratio_mismatch"]:
        print(f"QAlb ratio mismatch: {info['qalb_ratio_mismatch']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
