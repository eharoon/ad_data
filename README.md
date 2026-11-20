# ad_data

Data and analyses for the Alzheimer's disease (AD) line of work in the Emory Behavioral Immunology Program.

## Combined AD database

`scripts/build_combined.py` reads the Midlife source files (clinical, fluid biomarker, MRS and MRI tables) and merges them into one table with one row per participant and timepoint. Raw and merged participant data never enter git: `.gitignore` excludes every `.xlsx`/`.csv` except synthetic test fixtures and the generated dictionary.

| Path | Role |
|---|---|
| `config/sources.yaml` | Linking rules: for each source file, its ID column, how that ID maps to the canonical participant ID, its timepoint, and any renames |
| `scripts/build_combined.py` | Reads the sources, applies the rules, merges, and writes the outputs below |
| `output/<table>.csv` | Merged table(s), `combined.csv` by default; a source can be sent to a separate table such as a second cohort (git-ignored) |
| `output/conflicts.csv` | Every cell where two sources disagree (git-ignored) |
| `docs/data_dictionary.csv` | One row per variable: source file, sheet, original column name, rename |
| `docs/merge_qc_report.md` | Per-source counts, unmapped IDs, unmatched participants, duplicate keys, conflicting values |
| `tests/` | Synthetic data that exercises the merge and QC checks |

### Linking rules (confirmed 2026-11-20)

- Each participant is identified by `subject_key`: `MIDL001`–`MIDL092` for the Midlife study and `PHE001`–`PHE115` for Phenom. The prefix is needed because both cohorts reuse the numbers 1–92. The seven ID formats found in the source files (`1`, `001`, `M001`, `MIDL01`, `MidLife_subj001`, Haroon ID, `PHE001`) all convert to this key.
- Each cohort was seen once, so each table has one row per participant and no timepoint column.
- Midlife goes to `output/combined.csv` and Phenom to `output/phenom.csv`.
- Sources are listed in priority order. REDCap wins for demographics and group, and the original lab or scanner file wins over derived analysis files.
- Sex is coded 1 = male, 2 = female, and group 0 = control, 1 = depressed.

Some columns are held back until open data problems are resolved: the two ReHo cluster columns (labels may be swapped), two mislabeled ODI columns, and CSF albumin (shifted IDs). `config/sources.yaml` explains each one.

### Reference (master) file

`dat_harmonized.csv` (in `!ADgrant/R/ADMs`, written by `harmonize_data.qmd`) is the master analysis file and the provenance reference. When it is passed with `--reference`, the merge is checked against it column by column in `docs/reference_check.md`. The data dictionary's `reference_column` field also records which master column each merged variable corresponds to.

### Combined master (dat_combined.csv)

`dat_harmonized.csv` is the single master and stays unchanged. `scripts/build_master_combined.py` writes a second master, `dat_combined.csv`, which adds Midlife plasma albumin, CSF albumin and QAlb from `QAlbumin_discovery_values_2026-11-12.csv`. It also writes `dat_combined_provenance.md`, which records the SHA-256 of both inputs. The script stops if the master's hash differs from the confirmed version, or if any Midlife albumin row disagrees with the master on age or group.

### Running it

```
pip install -r requirements.txt
python scripts/build_combined.py --data-dir /path/to/01_Comb_folder \
    --reference "/path/to/!ADgrant/R/ADMs/dat_harmonized.csv"
python -m pytest tests
```

### Merge behaviour

- A source whose ID or timepoint rule is still `TODO` is skipped and listed in the QC report, so the script never guesses a link.
- Sources are joined with an outer join, so a participant present in any source appears in the table.
- When two sources supply the same variable, the source listed first in the config wins, the other fills gaps, and every disagreement is logged.
- Duplicate participant-timepoint keys within a source stop that source from merging unless its config says `on_duplicate: first`.

## Owner

Ebrahim Haroon, Emory University
