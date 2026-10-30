"""Run the merge on small synthetic files (no participant data)."""

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import build_combined  # noqa: E402

FIX = Path(__file__).resolve().parent / "fixtures"


def run(tmp_path):
    build_combined.main([
        "--config", str(FIX / "config.yaml"),
        "--out-dir", str(tmp_path / "out"),
        "--docs-dir", str(tmp_path / "docs"),
    ])
    combined = pd.read_csv(tmp_path / "out" / "combined.csv", dtype={"participant_id": str})
    conflicts = pd.read_csv(tmp_path / "out" / "conflicts.csv", dtype={"participant_id": str})
    dictionary = pd.read_csv(tmp_path / "docs" / "data_dictionary.csv")
    report = (tmp_path / "docs" / "merge_qc_report.md").read_text()
    return combined, conflicts, dictionary, report


def test_ids_normalised_and_outer_joined(tmp_path):
    combined, *_ = run(tmp_path)
    assert list(combined["participant_id"]) == ["001", "002", "003", "009", "PHE001", "PHE003"]
    assert set(combined["timepoint"]) == {"baseline"}
    row1 = combined.set_index("participant_id").loc["001"]
    assert row1["csf_il6"] == 3.1 and row1["hippo"] == 4000


def test_conflicts_keep_earlier_source(tmp_path):
    combined, conflicts, *_ = run(tmp_path)
    # clinical says 42 for participant 002, csf says 43: clinical (earlier) wins.
    assert combined.set_index("participant_id").loc["002", "age"] == 42
    assert list(conflicts["participant_id"]) == ["002"]
    # mri leaves 003's age blank, so no conflict and clinical's value stays.
    assert combined.set_index("participant_id").loc["003", "age"] == 50
    # 009 exists only in csf, so its age comes from csf.
    assert combined.set_index("participant_id").loc["009", "age"] == 60


def test_dictionary_records_source_and_rename(tmp_path):
    _, _, dictionary, _ = run(tmp_path)
    il6 = dictionary[dictionary["variable"] == "csf_il6"].iloc[0]
    assert il6["source"] == "csf" and il6["original_column"] == "IL6" and il6["renamed"]


def test_qc_report_flags_problems(tmp_path):
    *_, report = run(tmp_path)
    assert "awaiting rules" in report               # pending source skipped
    assert "**mri**: ABC" in report                 # unparseable ID
    assert "002, baseline" in report                # duplicate key in csf
    assert "1 not in roster (009)" in report        # unmatched participant
