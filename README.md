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

### Running it

```
pip install -r requirements.txt
python scripts/build_combined.py --data-dir /path/to/01_Comb_folder
python -m pytest tests
```

### Merge behaviour

- A source whose ID or timepoint rule is still `TODO` is skipped and listed in the QC report, so the script never guesses a link.
- Sources are joined with an outer join, so a participant present in any source appears in the table.
- When two sources supply the same variable, the source listed first in the config wins, the other fills gaps, and every disagreement is logged.
- Duplicate participant-timepoint keys within a source stop that source from merging unless its config says `on_duplicate: first`.

## Owner

Ebrahim Haroon, Emory University
