#!/usr/bin/env python3
"""Build the combined master from dat_harmonized.csv plus Midlife albumin.

dat_harmonized.csv (!ADgrant/R/ADMs, written by harmonize_data.qmd) is the
single master and provenance file. This script never edits it. It adds the
Midlife (discovery) plasma albumin, CSF albumin and albumin quotient (QAlb)
from the lab workbook MIDLIFE_Albumin_20261026.xlsx to the Mlife rows, the same
way qalb_adjustment_2026-11-12.qmd does, and writes the result as a second
master, dat_combined.csv, with a provenance note beside it.

The workbook gives duplicate CSF (V1, V2) and plasma (VP1, VP2) readings per
participant; the means (Vmean, Vpmean, in g/dL) are used, and QAlb is
CSF/PLASMA x 1000. Lab ID 25 is relabelled 26 (owner-final 2026-11-12: there
is no Midlife participant 25 with CSF, and 26 is the one missing from the lab
sheet).

Phenom rows already carry plasma albumin, CSF albumin and QAlb in the master
and are left exactly as they are.

Usage:
  python scripts/build_master_combined.py \\
      --master  ".../R/ADMs/dat_harmonized.csv" \\
      --albumin ".../MIDLIFE_Albumin_20261026.xlsx" \\
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

# master column <- lab-workbook column
ALBUMIN = {
    "plasma_albumin_gdl": "Vpmean",
    "csf_albumin_gdl": "Vmean",
    "qalbumin": "qalb_x1000",
}
ID_RELABEL = {25: 26}  # owner-final 2026-11-12 (see qalb_adjustment_2026-11-12.qmd)
HEADER_ROW = 4         # rows 0-3 hold the title, date and CSF/Plasma banner


def read_lab(path: Path) -> pd.DataFrame:
    lab = pd.read_excel(path, header=HEADER_ROW)
    lab = lab.dropna(subset=["ID"])          # trailing blank and summary rows
    lab["id"] = lab["ID"].astype(int).replace(ID_RELABEL)
    lab["qalb_x1000"] = lab["CSF/PLASMA"] * 1000
    return lab


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(master_path: Path, lab_path: Path, allow_new_master: bool = False):
    digest = sha256(master_path)
    if digest != MASTER_SHA256 and not allow_new_master:
        sys.exit(
            f"{master_path.name} has changed since it was confirmed as the master "
            f"(sha256 {digest[:12]}..., expected {MASTER_SHA256[:12]}...). "
            "Confirm the new version, then rerun with --allow-new-master."
        )
    master = pd.read_csv(master_path)
    lab = read_lab(lab_path)

    if lab["id"].duplicated().any():
        sys.exit(f"duplicate lab ids after relabelling: {sorted(lab.loc[lab['id'].duplicated(), 'id'])}")
    mlife = master["study"] == "Mlife"
    if master.loc[mlife, list(ALBUMIN)].notna().any(axis=None):
        sys.exit("The master already holds Mlife albumin values; refusing to overwrite them.")

    # The lab sheet must cover exactly the Midlife participants with CSF.
    with_csf = set(master.loc[mlife & (master["csf"] == 1), "id"])
    extra, absent = sorted(set(lab["id"]) - with_csf), sorted(with_csf - set(lab["id"]))
    if extra or absent:
        sys.exit(f"Lab ids do not match Mlife csf == 1: not in master {extra}; missing from lab {absent}")
    # CSF/PLASMA in the sheet must equal Vmean / Vpmean.
    if not np.allclose(lab["CSF/PLASMA"], lab["Vmean"] / lab["Vpmean"], rtol=1e-6):
        sys.exit("CSF/PLASMA column does not equal Vmean / Vpmean")

    combined = master.copy()
    lookup = lab.set_index("id")
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
        "lab_sha256": sha256(lab_path),
        "n_rows": len(combined),
        "filled": {c: int(combined.loc[mlife, c].notna().sum()) for c in ALBUMIN},
        "qalb_ratio_mismatch": off.values.tolist(),
    }
    return combined, info


def write_provenance(path: Path, master_path: Path, lab_path: Path, info: dict):
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
| Midlife albumin (lab workbook) | `{lab_path.name}` | `{info['lab_sha256']}` |

## What was added

`dat_combined.csv` is `dat_harmonized.csv` with Midlife (study = Mlife) albumin filled in. All other cells are identical to the master. Phenom albumin values come from the master unchanged.

| Column | Lab column | Mlife participants filled |
|---|---|---|
{filled}

Rows are matched on `id` within study = Mlife. The lab IDs, after relabelling lab ID 25 as 26 (owner-final 2026-11-12), equal exactly the Midlife participants with `csf == 1`. Albumin values are the means of the duplicate readings in g/dL, and QAlb is CSF/plasma x 1000.

{mismatch}

Rows: {info['n_rows']}.
""")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--master", type=Path, required=True)
    ap.add_argument("--albumin", type=Path, required=True, help="MIDLIFE_Albumin lab workbook (.xlsx)")
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--allow-new-master", action="store_true")
    args = ap.parse_args(argv)

    combined, info = build(args.master, args.albumin, args.allow_new_master)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    combined.to_csv(args.out_dir / "dat_combined.csv", index=False)
    write_provenance(args.out_dir / "dat_combined_provenance.md", args.master, args.albumin, info)
    print(f"dat_combined.csv: {info['n_rows']} rows; Mlife filled {info['filled']}")
    if info["qalb_ratio_mismatch"]:
        print(f"QAlb ratio mismatch: {info['qalb_ratio_mismatch']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
