"""Synthetic check of the combined-master build (no participant data)."""

import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import build_master_combined as bmc  # noqa: E402


def make(tmp_path, disc_age=50.2):
    master = pd.DataFrame({
        "id": [1, 2, 1], "study": ["Mlife", "Mlife", "Phenom"], "age": [50.0, 60.0, 40.0],
        "subgrp": [1, 0, 1], "ctnfr2": [1.0, 2.0, 3.0],
        "plasma_albumin_gdl": [None, None, 3.0], "csf_albumin_gdl": [None, None, 0.03], "qalbumin": [None, None, 10.0],
    })
    disc = pd.DataFrame({"id": [1], "age": [disc_age], "subgrp": [1], "plasma_alb_mean_gdl": [4.0],
                         "csf_alb_mean_gdl": [0.024], "qalb_x1000": [6.0]})
    mp, qp = tmp_path / "dat_harmonized.csv", tmp_path / "q.csv"
    master.to_csv(mp, index=False)
    disc.to_csv(qp, index=False)
    return mp, qp, master


def test_fills_mlife_only(tmp_path, monkeypatch):
    mp, qp, master = make(tmp_path)
    monkeypatch.setattr(bmc, "MASTER_SHA256", bmc.sha256(mp))
    monkeypatch.setattr(bmc, "EXPECTED_MATCHES", 1)
    out, info = bmc.build(mp, qp)
    assert out.loc[0, "qalbumin"] == 6.0 and pd.isna(out.loc[1, "qalbumin"])
    assert out.loc[2, "qalbumin"] == 10.0                     # Phenom untouched
    assert out["ctnfr2"].equals(master["ctnfr2"])
    assert info["qalb_ratio_mismatch"] == []


def test_rejects_changed_master_and_identity_mismatch(tmp_path, monkeypatch):
    mp, qp, _ = make(tmp_path, disc_age=55.0)
    with pytest.raises(SystemExit):
        bmc.build(mp, qp)                                      # hash differs
    monkeypatch.setattr(bmc, "MASTER_SHA256", bmc.sha256(mp))
    monkeypatch.setattr(bmc, "EXPECTED_MATCHES", 1)
    with pytest.raises(SystemExit):
        bmc.build(mp, qp)                                      # age off by 5 y
