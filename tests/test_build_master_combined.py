"""Synthetic check of the combined-master build (no participant data)."""

import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import build_master_combined as bmc  # noqa: E402


def make(tmp_path, lab_ids=(1, 25)):
    master = pd.DataFrame({
        "id": [1, 2, 26, 1], "study": ["Mlife", "Mlife", "Mlife", "Phenom"], "csf": [1, 0, 1, 1],
        "ctnfr2": [1.0, 2.0, 3.0, 4.0],
        "plasma_albumin_gdl": [None, None, None, 3.0], "csf_albumin_gdl": [None, None, None, 0.03],
        "qalbumin": [None, None, None, 10.0],
    })
    vm, vp = [0.024, 0.030], [4.0, 5.0]
    body = pd.DataFrame({"Count": [1, 2], "ID": list(lab_ids), "Vmean": vm, "Vpmean": vp,
                         "CSF/PLASMA": [a / b for a, b in zip(vm, vp)]})
    lab = tmp_path / "lab.xlsx"
    with pd.ExcelWriter(lab) as xw:   # four banner rows above the header, as in the lab sheet
        body.to_excel(xw, index=False, startrow=bmc.HEADER_ROW)
    mp = tmp_path / "dat_harmonized.csv"
    master.to_csv(mp, index=False)
    return mp, lab, master


def test_fills_mlife_with_relabel(tmp_path, monkeypatch):
    mp, lab, master = make(tmp_path)
    monkeypatch.setattr(bmc, "MASTER_SHA256", bmc.sha256(mp))
    out, info = bmc.build(mp, lab)
    assert out.loc[0, "qalbumin"] == pytest.approx(6.0)
    assert out.loc[2, "qalbumin"] == pytest.approx(6.0)        # lab 25 -> id 26
    assert pd.isna(out.loc[1, "qalbumin"])                       # no CSF
    assert out.loc[3, "qalbumin"] == 10.0                        # Phenom untouched
    assert out["ctnfr2"].equals(master["ctnfr2"])


def test_rejects_changed_master_and_wrong_ids(tmp_path, monkeypatch):
    mp, lab, _ = make(tmp_path, lab_ids=(1, 2))
    with pytest.raises(SystemExit):
        bmc.build(mp, lab)                                       # hash differs
    monkeypatch.setattr(bmc, "MASTER_SHA256", bmc.sha256(mp))
    with pytest.raises(SystemExit):
        bmc.build(mp, lab)                                       # id 2 has no CSF
