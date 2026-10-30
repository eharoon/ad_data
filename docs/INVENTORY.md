# Inventory of AD source data files (01_Comb_folder)

Inventory date: 2026-10-30. Source folder: `01_Comb_folder` (53 files). No source file was modified.
The full list of every column in every sheet, with its non-missing count and an example value, is in [`column_catalog.csv`](column_catalog.csv) (3,679 rows).

## Summary

The folder holds two separate cohorts, and each was measured at a single visit, so the composite database can be one row per participant with no timepoint join.

- **Midlife** (the MRS in Midlife Depression study) is the main cohort and carries all the AD markers. It has 92 enrolled record IDs (1 to 92), of which 83 have imaging and plasma, 81 have CANTAB cognition, and 54 have CSF. Every Midlife file can be linked through the REDCap `record_id`, but the ID is written in seven different formats across files (see the linking rules below).
- **Phenom** is a second, earlier cohort (IDs 1 to 115, `PHE###`). Its files carry immune, metabolic, cognitive and MRS data, but its AD-marker columns (`pnfl`, `pgfap`, and so on) are empty. Phenom and Midlife ID numbers overlap (both use 1 to 92), so the two cohorts must never be joined on the bare number.

I found eight data problems that affect linking. Three of them (an ID shift in the albumin file, swapped ReHo labels, and duplicated DTI columns) would silently attach values to the wrong participant or variable if merged as-is. They are listed under "Data problems found".

## Proposed linking rules (for your confirmation)

### Rule 1. Participant key

I propose one key, `subject_key`, built as the study prefix plus the three-digit record number: `MIDL001` to `MIDL092` for Midlife and `PHE001` to `PHE115` for Phenom. The table shows how each existing ID format converts to it.

| ID format in the file | Example | Files | Conversion to `subject_key` |
|---|---|---|---|
| `record_id`, integer | `1` | REDCap exports (demographics, demographics_master, MRSInMidlifeDepressi), metabolic file, roi* files | `MIDL` + zero-padded 3 digits |
| `SubjID` or `id`, integer | `1` | FreeSurfer cortical/subcortical, DTI, xtract, ReHo, diffusion-correlation files | same as above |
| `SubjID`, zero-padded text | `001` | MRS single-voxel CSVs | `MIDL` + the text as is |
| `Subject ID`, zero-padded text | `001` | CANTAB files (subjects, RowBySession, RowByMeasure) | `MIDL` + the text as is |
| `MidLife_subj###` | `MidLife_subj001` | FreeSurfer amygdala, hippocampus, thalamus files | replace `MidLife_subj` with `MIDL` |
| `M###` | `M001` | `!PlasmaImm_Source`, `!CSFImm_Source` | replace `M` with `MIDL` |
| `Haroon ID`, integer | `11` | `!ADsource` (all sheets) | `MIDL` + zero-padded 3 digits |
| `unique_id`, `MIDL##` | `MIDL01` | metabolic file | `MIDL` + number re-padded to 3 digits |
| `id` / `ID`, integer, with `study = Phenom` | `14` | `phenom_with_metabolics.csv`, `Phenom_Master_F.xlsx` | `PHE` + zero-padded 3 digits |
| `subject_id`, `PHE###` | `PHE001` | `alb_phenom.xlsx` | as is |

Two checks support treating all of these as the same Midlife number. First, the `Haroon ID` set in `!ADsource` is identical to the `M###` set in the immune source files (83 plasma, 54 CSF). Second, the immune values in the metabolic file match `!PlasmaImm_Source` exactly when joined on `record_id` = `M###` (81 of 81 participants for IL-6 and hsCRP).

### Rule 2. Timepoint

No timepoint key is needed, because every participant contributes one visit per file. The visit labels that do exist are listed below so they can be stored as metadata rather than used for joining.

| Cohort | Label in file | Where it appears | Meaning |
|---|---|---|---|
| Midlife | `screening_visit_arm_1` | demographics, demographics_master | REDCap screening event |
| Midlife | `visit_1_scanning_arm_1` | MRSInMidlifeDepressi (IDS-SR items) | REDCap scan-day event |
| Midlife | `Day 1` | all CANTAB files | CANTAB session |
| Midlife | none | imaging, MRS, blood files | single acquisition |
| Phenom | `inpatient_day_2_arm_1` | alb_phenom (plasma albumin) | inpatient day 2 |
| Phenom | `inpatient_day_3_arm_1` | alb_phenom (CSF albumin) | inpatient day 3 |

I propose one row per participant. If a later wave is added, a `visit` column can be introduced then.

### Rule 3. Canonical coding

| Variable | Codings found | Proposed canonical form |
|---|---|---|
| Sex | REDCap `gender` 1 = male, 2 = female; CANTAB `Gender` same; metabolic `sex` 0 = male, 1 = female; Phenom `fem` 1 = female | `sex`: 1 = male, 2 = female (REDCap dictionary) |
| Group | REDCap `group_control_depressed` 0 = control, 1 = depressed; CANTAB `Group` "Healthy Volunteers"/"Depressed"; Phenom `subgrp_f` "MDD" | `group`: 0 = control, 1 = depressed |
| Age | `age` (integer) and `cage` (decimal years at HAM-D date) in demographics_master; `age` in metabolic; `age` in Phenom | keep `age` (integer) and add `age_exact` from `cage` |
| Date of birth | REDCap `dob` (yyyy-mm-dd); CANTAB `Date of birth` (mm/dd/yy) | REDCap `dob` |
| Race | `race` (REDCap codes 1 to 6), `r_a_c_e` (recoded), `race_white` | keep REDCap `race`; carry `race_white` as derived |

When two sources disagree, I propose REDCap wins for demographics and group, and the original lab or acquisition file wins for biomarker and imaging values (rather than a downstream analysis file).

### Rule 4. Variable renames

Each measured quantity should appear once, under a name that states compartment and unit. The table lists every variable I found under more than one name.

| Quantity | Names found (file) | Proposed name |
|---|---|---|
| Plasma NfL | `PNFL-light (pg/mL(` (ADsource/plasma); `pg/mL NFL-light` (ADsource/Sheet1); `pnfl` (phenom_with_metabolics, empty) | `p_nfl_pgml` |
| Plasma GFAP | `P GFAP (pg/mL  )`; `pg/mL GFAP`; `pgfap`; `qpgfap` in diffusion sheet names | `p_gfap_pgml` |
| Plasma Aβ42, Aβ40 | `P Abeta-42 (pg/mL )`, `P Abeta-40 (pg/mL)`; `pa42`, `pa40`; `qpa42`, `qpa4240` (sheet names) | `p_ab42_pgml`, `p_ab40_pgml`, `p_ab42_40_ratio` |
| Plasma pTau181 | `P  pTau 181 (pg/mL )`; `pTau 181 v2` (Sheet1); `ptau` | `p_ptau181_pgml` |
| Plasma BDNF | `P BDNF (pg/mL )`; `pg/mL BDNF`; `pbdnf` | `p_bdnf_pgml` |
| CSF AD markers | `c NFL-light`, `c GFAP`, `c Abeta-42`, `c Abeta-40`, `c pTau 181`, `c BDNF` (ADsource/CSF); `cnfl`, `cgfap`, `ca42`, … (Phenom) | `c_nfl_pgml`, `c_gfap_pgml`, and so on |
| CSF Aβ42/40 ratio | `Abeta 42:40 ratio` (ADsource/Sheet2 only); `ca4240` | `c_ab42_40_ratio` |
| Plasma IL-6 | `IL6 (pg/ml)` (PlasmaImm); `il6` (metabolic); `plasma_il6_pgml` (metabolic Units sheet); `pil6` (Phenom) | `p_il6_pgml` |
| Plasma TNF | `TNF-alpha (pg/ml)`; `tnf`; `ptnf` | `p_tnf_pgml` |
| Plasma TNFR2 | `TNF RII (pg/ml)` (PlasmaImm, pg/mL); `tnfrii` (metabolic, ng/mL); `ptnfr2` | `p_tnfr2_pgml` |
| Plasma sIL-6R | `IL6sr_1`, `IL6sr_2` (PlasmaImm, pg/mL); `il6sr` (metabolic, ng/mL, equals replicate 2) | `p_il6sr_pgml` |
| Plasma IL-1ra | `IL-1ra_1`, `IL-1ra_2` (pg/mL); `il1ra` (metabolic, ng/mL, equals replicate 2) | `p_il1ra_pgml` |
| Plasma MCP-1 | `MCP1_1`, `MCP1_2`; `mcp1` (metabolic, equals replicate 2) | `p_mcp1_pgml` |
| Plasma hsCRP | `hsCRP (mg/l)` (PlasmaImm); `hsCRP` (metabolic); `pcrp`, `hsCRP` (Phenom); `screeningCRP` (clinical lab, metabolic) | `p_hscrp_mgl`; keep `screening_crp_mgl` separate |
| CSF hsCRP | `hsCRP (mg/l)` and `hsCRP (pg/ml)` (same value, two units, CSFImm) | `c_hscrp_mgl` |
| CSF TNFR2 | `TNF RII (pg/ml)` (CSFImm); `ctnfr2`; `qctnfr2` (sheet names) | `c_tnfr2_pgml` |
| TG/HDL ratio | `tg_hdl_ratio` (metabolic and roi* files, identical values); `tg_hdl` (Phenom) | `tg_hdl_ratio` |
| Leptin, insulin | `Leptin`, `INS` (metabolic and Phenom); `z_log10_Leptin`, `z_log10_INS` (also in roi* files, identical) | keep raw; store transforms once |
| Intracranial volume | `eTIV` (6 cortical files); `EstimatedTotalIntraCranialVol` (subcortical); identical values | `etiv` |
| Brain volume | `BrainSegVolNotVent` (all 7 FreeSurfer files) | `brainsegvolnotvent`, stored once |
| ReHo | `gReHo`, `a42ReHo`, `pgfReHo` (rehocomb); `ReHo` (sheets `ReHo-qpa42`, `ReHo-qpgfap`) | see problem 2 before naming |
| DTI TNFR2 tracts | `ctnfr16fa` = `cs16LFAifa`; `ctnfr03md` = `csRAF3imd`; `ctnfr07md` = `csRATR7imd`; `ctnfr03fso` = `cp3RAFifso` | keep the longer `20230406_ctnfr2_dti` names; drop `dti_ctnfr2` duplicates |
| IDS-SR total | `ids_sr_score` (REDCap); `ids_tot_minus_app_wt` (metabolic, excludes appetite and weight items); `idssr` (Phenom) | keep both Midlife scores; they are different variables |

## Data problems found

These are listed in order of how much damage they would do if merged unchanged.

1. **`alb_phenom.xlsx`: the day-3 ID column is shifted by one row from PHE034 onward.** The day-2 column reads PHE034, PHE035, … while the day-3 column on the same rows reads PHE035, PHE036, …, because a REDCap export of two events was pasted side by side. The CSF albumin value on each of those 74 rows may therefore belong to the next participant. The fix depends on which ID column the CSF value was exported with; I recommend re-exporting this from REDCap rather than guessing.
2. **ReHo labels are swapped between two files.** In `rehocomb.xlsx`, `a42ReHo` holds the values that `midlife-ReHo-biomaker-correlation-roi-mean.xlsx` labels `ReHo-qpgfap`, and `pgfReHo` holds the values labeled `ReHo-qpa42`. One of the two files is mislabeled; the analyst who ran the ReHo correlations would know which.
3. **`20230406_ctnfr2_dti.xlsx`: two "ODI" columns are copies of FISO columns.** `cs16LFAoodi` is identical to `cp3RAFofso`, and `cs16LFAiodi` is identical to `cp3RAFifso`. The true ODI values for that tract are not in this file. Separately, `ctnfr34md` and `ctnf16odi` in `dti_ctnfr2.xlsx` have no match in the 20230406 file.
4. **Date of birth disagrees between REDCap and CANTAB for two participants.** Record 41: REDCap 2018-05-23, CANTAB 1955-05-25 (the REDCap value is impossible). Record 57: REDCap 1982-07-14, CANTAB 1981-07-14.
5. **Sex disagrees for record 70.** REDCap `gender` = 1 (male), CANTAB `Gender` = 2 (female). The metabolic file agrees with REDCap.
6. **Group disagrees for record 19.** REDCap and the metabolic file code control (0); CANTAB codes "Depressed".
7. **Units differ for the same immune marker.** The metabolic file reports TNFR2, sIL-6R and IL-1ra in ng/mL (the source value in pg/mL divided by 1,000) and silently uses replicate 2 where the source has two replicates. The replicates differ for 31 participants on MCP-1 and 19 on sIL-6R and IL-1ra. You need to decide whether the composite uses replicate 2 (to match published analyses) or the mean.
8. **Records with no data and do-not-complete flags.** The metabolic file has 7 rows (MIDL28, 40, 42, 58, 60, 71, 91) with a group code but no `record_id` or measurements. `demographics_master.xlsx` flags records 6, 29, 42, 58, 60 and 71 in a `DNC` column ("Claus" or "Failed Comfort"). Record 6 has no imaging, which fits. These should be kept in the roster with a status flag rather than dropped silently.

Minor issues that do not affect linking: the CSF sample for Haroon ID 33 is annotated "appeared to have blood contamination" (ADsource/Sheet2); CSF hsCRP is given twice in two units; `Phenom_Master_F.xlsx` contains 9 Phenom IDs (15, 22, 26, 42, 52, 87, 90, 96, 109) that are absent from `phenom_with_metabolics.csv`.

## File inventory

Row counts below are participants (data rows), not spreadsheet rows. "Visit" is blank when the file has no visit column.

### Midlife: roster, demographics and clinical

| File / sheet | Rows | Cols | ID column (format) | Visit | Contents |
|---|---|---|---|---|---|
| `demographics.xlsx` / demographics | 92 | 34 | `record_id` (int); also `record_id_13f0fc` | `redcap_event_name` = screening_visit_arm_1 | REDCap demographics form: DOB, gender, education, income, race, ethnicity, living situation, children, sexual identity |
| `demographics_master.xlsx` / MRSInMidlifeDepressi-EHdemograp | 90 (no 91, 92) | 33 named + 2 blank | `record_id` (int) | screening_visit_arm_1 | Curated demographics plus HAM-D date, exact age (`cage`), episode history, smoking, antidepressant count, bipolarity index, BMI, recoded race, group, DNC flag |
| `MRSInMidlifeDepressi.xlsx` | 87 (no 28, 40, 58, 60, 71) | 41 | `record_id` (int) | `redcap_event_name` = visit_1_scanning_arm_1 | IDS-SR 30 items, total score, completion date, appetite items |
| `Midlife_metabolic_markers_07.16.26.xlsx` / Midlife_Behavior, Plasma data_0 | 92 (85 with data) | 80 | `unique_id` (`MIDL##`) and `record_id` (float) | none | Analysis-ready file: demographics, appetite, IDS-SR subscores, MFI fatigue, A1C, TG/HDL, insulin, glucose, leptin, CRP, 7 plasma cytokines with log10, ln and z transforms. Header is on row 2; row 1 holds section labels |
| same / Units | 11 | 2 | n/a | n/a | Units for insulin, glucose, leptin and plasma cytokines |
| `Data_dictionary.xlsx` / MRSInMidlifeDepression_DataDict | 666 fields | 18 | n/a | n/a | REDCap data dictionary for 35 forms (HAM-D, IDS-SR, PSQI, CTQ, MFI, SHAPS, STAI, vitals, LP vitals, meds, adverse events, and others). Most of these forms are not yet exported in the folder |

### Midlife: biomarkers

| File / sheet | Rows | Cols | ID column (format) | Contents |
|---|---|---|---|---|
| `!ADsource.xlsx` / plasma | 83 | 8 | `Haroon ID` (int) | Quanterix plasma NfL, GFAP, Aβ42, Aβ40, pTau181, BDNF (pg/mL), plate position |
| `!ADsource.xlsx` / CSF | 54 | 8 | `Haroon ID` (int) | Same six markers in CSF |
| `!ADsource.xlsx` / Sheet1 | 83 | 8 | `Haroon ID` | Exact copy of the plasma sheet with different headers |
| `!ADsource.xlsx` / Sheet2 | 54 | 10 | `Haroon ID` | Copy of the CSF sheet plus Aβ42:40 ratio and a sample note |
| `!PlasmaImm_Source.xlsx` / Sheet1 | 83 | 12 | `Assay/ Patient ID` (`M###`) | Plasma hsCRP (mg/L), TNF, IL-1β, IL-6, TNFR2, and duplicate assays of MCP-1, sIL-6R, IL-1ra (pg/mL) |
| `!CSFImm_Source.xlsx` / Sheet1 | 54 | 10 | `Assay/ Patient ID` (`M###`) | CSF hsCRP (mg/L and pg/mL), TNF, IL-1β, IL-6, MCP-1, sIL-6R, IL-1ra, TNFR2 |

### Midlife: cognition (CANTAB)

All CANTAB files code the visit as `Day 1` and carry name, date of birth, gender and group.

| File | Rows | Cols | ID column (format) | Contents |
|---|---|---|---|---|
| `subjects_Midlife.csv` | 81 | 9 | `Subject ID` (`001`) | Roster: DOB, gender, language, group |
| `RowBySession_Midlife.csv` | 81 | 106 | `Subject ID` | One row per participant: RTI, DMS and SWM summary scores |
| `RowBySessionNorms_Midlife.csv` | 81 | 107 | `Subject ID` | Same scores plus a language column; no normed values |
| `RowByMeasure_Midlife.csv` | 6,480 | 24 | `Subject ID` | Long format, 80 measure codes per participant |
| `RowByMeasureNorms_Midlife.csv` | 6,480 | 27 | `Subject ID` | Same as above; the Standard Score, Percentile and Norms Bank columns are empty |

### Midlife: MRI structure (FreeSurfer)

All have the same 83 participants: record IDs 1 to 92 except 6, 28, 29, 40, 42, 58, 60, 71 and 91. The diffusion, xtract and MRS files share this set, except that PCC MRS also lacks 83 and the ReHo files also lack 48 and 53. For comparison, CANTAB lacks 28, 29, 40, 42, 58, 59, 60, 71, 87, 91, 92, and plasma lacks 18, 21, 28, 29, 40, 58, 60, 91, 92.

| File | Cols | ID column (format) | Contents |
|---|---|---|---|
| `lh_` / `rh_cortical_area.xlsx` | 38 | `id` (int) | Desikan regional surface area, total white-surface area, BrainSegVolNotVent, eTIV |
| `lh_` / `rh_cortical_thickness.xlsx` | 38 | `id` (int) | Regional and mean cortical thickness, BrainSegVolNotVent, eTIV |
| `lh_` / `rh_cortical_volume.xlsx` | 37 | `id` (int) | Regional cortical volume, BrainSegVolNotVent, eTIV |
| `subcortical_volume.xlsx` | 53 | `id` (int) | aseg volumes (ventricles, thalamus, caudate, putamen, hippocampus, amygdala, white matter hypointensities, global volumes) |
| `MidLife-amygdalar-nuclei.lh/rh-v22.xlsx` | 11 | `SubjID` (`MidLife_subj###`) | 9 amygdala nuclei and whole amygdala (FreeSurfer v22) |
| `MidLife-hipposubfields.lh/rh-v22.xlsx` | 23 | `SubjID` (`MidLife_subj###`) | 19 hippocampal subfields, head, body, whole (v22) |
| `MidLife-thalamic-nuclei.lh/rh-v13.xlsx` | 27 | `SubjID` (`MidLife_subj###`) | 25 thalamic nuclei and whole thalamus (v13) |

### Midlife: MRS, diffusion and resting-state

| File / sheet | Rows | Cols | ID column (format) | Contents |
|---|---|---|---|---|
| `MidLife-ACC-MRS-single-voxel.csv` | 83 | 23 | `SubjID` (`001`) | ACC voxel: water signal, linewidth, SNR, and Glu, Glx, mI, Cho, NAA, Cr concentration, SD and ratio to Cr |
| `MidLife-PCC-MRS-single-voxel.csv` | 82 | 23 | `SubjID` (`001`) | Same metrics, PCC voxel |
| `MidLife-L_Basal-MRS-single-voxel.csv` | 83 | 23 | `SubjID` (`001`) | Same metrics, left basal ganglia |
| `MidLife-R_Basal-MRS-single-voxel.csv` | 83 | 23 | `SubjID` (`001`) | Same metrics, right basal ganglia |
| `midlife_xtract.xlsx` / Midlife-xtract-stats(76) | 83 | 295 | `SubjID` (int) | XTRACT tract volume, length, FA, MD, NODDI ficvf, fiso, odi for 42 tracts (left/right) |
| `midlife_xtract_glossary.xlsx` | 23 | 3 | n/a | Tract abbreviations and descriptions |
| `dti_combined.xlsx` | 83 | 41 | `SubjID` plus repeated `SubjID2`–`SubjID4` (identical) | Selected FA, FICV, FISO, ODI tract values (t05 to t42) |
| `dti_ctnfr2.xlsx` | 83 | 7 | `SubjID` (int) | Six DTI values from tracts that correlated with CSF TNFR2 |
| `20230406_ctnfr2_dti.xlsx` / Sheet1 | 83 | 21 | `SubjID` (int) | 20 tract values (FA, MD, FISO, ODI; inside/outside significant cluster) |
| `20230406_ctnfr2_dti.xlsx` / Sheet2 | 22 | 5 | n/a | Lookup from tract labels to column names |
| `rehocomb.xlsx` | 81 | 4 | `SubjID` (int) | Global ReHo and two ReHo cluster means |

### Midlife: analysis outputs (cluster or ROI means from completed correlations)

These files hold values extracted from clusters that were defined by correlating imaging with a biomarker. They are results of earlier analyses rather than source measurements, and their contents depend on the analysis that produced them.

| File | Rows | ID column | Contents |
|---|---|---|---|
| `midlife-diffusion-admarker-correlation-depressed-roi-mean.xlsx` (11 sheets) | 83 | `SubjID` (int), header on row 2 | Mean FA, MD, ficvf, fiso, odi in clusters correlated (Pearson and Spearman blocks side by side) with plasma GFAP, NfL, Aβ42/40 |
| `midlife-diffusion-tnfr2-correlation-depressed-roi-mean.xlsx` (6 sheets) | 83 | same | Same for CSF and plasma TNFR2 |
| `midlife-ReHo-biomaker-correlation-roi-mean.xlsx` (2 sheets) | 81 | `SubjID` (int) | ReHo cluster means for Aβ42 and GFAP (labels swapped; problem 2) |
| `roi67-…`, `roi73-…`, `roi1004-…`, `roi1009-…`, `roi1010-…` (10 files) | 77 to 79 | `record_id` (int) | The metabolic predictor (TG/HDL, z-log leptin or insulin, identical to the metabolic file) followed by 1 to 17 cluster means |

### Phenom cohort

| File / sheet | Rows | Cols | ID column (format) | Visit | Contents |
|---|---|---|---|---|---|
| `phenom_with_metabolics.csv` | 72 | 163 | `id` (int) with `study` = Phenom; also `ad_id` (equals `id` where present) | none | Demographics, APOE genotype, plasma and CSF cytokines, kynurenine pathway, cognition, depression and fatigue scales, selected imaging values, lipid and metabolic panel. AD-marker columns exist but are empty |
| `Phenom_Master_F.xlsx` | 49 | 1,856 | `ID` (int) | none | Legacy wide analysis file: MRS, immune, cognition, FreeSurfer, resting-state connectivity, factor scores, transformed and regression-derived variables |
| `alb_phenom.xlsx` | 95 | 4 | `subject_id` (`PHE###`), given twice | inpatient_day_2_arm_1 / inpatient_day_3_arm_1 | Plasma albumin (day 2) and CSF albumin (day 3); ID shift (problem 1) |

### Not data

| File | Note |
|---|---|
| `booking.ics` | A calendar invitation for an EPCS enrollment appointment; unrelated to the study. Exclude. |

## Proposed scope for the composite

I propose the composite include the Midlife source files listed above (roster, demographics, clinical, AD and immune biomarkers, CANTAB `RowBySession`, FreeSurfer, MRS, xtract, and the TNFR2 DTI and ReHo files once problems 2 and 3 are resolved), keyed on `subject_key`. I propose leaving out the duplicate sheets (`!ADsource` Sheet1, the CANTAB "Norms" files, `dti_ctnfr2.xlsx`), the long-format `RowByMeasure` file, the cluster-mean analysis outputs, and `booking.ics`. Phenom would be a second table with the same key format, because it has no AD markers and a different measurement set.
