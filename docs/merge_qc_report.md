# Merge QC report

Generated 2026-11-20 21:05 UTC by `scripts/build_combined.py`.

## Summary

- `combined.csv`: 92 rows, 92 participants and 1099 variables from 30 sources.
- `phenom.csv`: 98 rows, 98 participants and 2002 variables from 3 sources.

## Sources

| Source | Status | Rows read | Rows kept | Participants | Note |
|---|---|---|---|---|---|
| demographics_master | merged | 90 | 90 | 90 |  |
| demographics | merged | 92 | 92 | 92 |  |
| redcap_ids_sr | merged | 87 | 87 | 87 |  |
| ad_plasma | merged | 83 | 83 | 83 |  |
| ad_csf | merged | 54 | 54 | 54 |  |
| plasma_immune | merged | 83 | 83 | 83 |  |
| csf_immune | merged | 54 | 54 | 54 |  |
| metabolic_markers | merged | 92 | 92 | 92 |  |
| cantab_session | merged | 81 | 81 | 81 |  |
| mrs_acc | merged | 83 | 83 | 83 |  |
| mrs_pcc | merged | 82 | 82 | 82 |  |
| mrs_l_basal | merged | 83 | 83 | 83 |  |
| mrs_r_basal | merged | 83 | 83 | 83 |  |
| lh_cortical_area | merged | 83 | 83 | 83 |  |
| rh_cortical_area | merged | 83 | 83 | 83 |  |
| lh_cortical_thickness | merged | 83 | 83 | 83 |  |
| rh_cortical_thickness | merged | 83 | 83 | 83 |  |
| lh_cortical_volume | merged | 83 | 83 | 83 |  |
| rh_cortical_volume | merged | 83 | 83 | 83 |  |
| subcortical_volume | merged | 83 | 83 | 83 |  |
| hippo_lh | merged | 83 | 83 | 83 |  |
| hippo_rh | merged | 83 | 83 | 83 |  |
| amygdala_lh | merged | 83 | 83 | 83 |  |
| amygdala_rh | merged | 83 | 83 | 83 |  |
| thalamus_lh | merged | 83 | 83 | 83 |  |
| thalamus_rh | merged | 83 | 83 | 83 |  |
| xtract | merged | 83 | 83 | 83 |  |
| dti_combined | merged | 83 | 83 | 83 |  |
| dti_ctnfr2_20230406 | merged | 83 | 83 | 83 |  |
| reho | merged | 81 | 81 | 81 |  |
| dti_ctnfr2 | excluded |  |  |  | duplicates columns of 20230406_ctnfr2_dti |
| cantab_measure_long | excluded |  |  |  | long format (one row per measure); RowBySession holds the summary scores |
| phenom_with_metabolics | merged | 72 | 72 | 72 |  |
| phenom_master | merged | 49 | 49 | 49 |  |
| albumin | merged | 95 | 95 | 95 |  |

## IDs that could not be mapped

None.

## Timepoint values with no mapping

None.

## Unmatched participants

`combined`, checked against the roster source `demographics` (92 participants):

- **demographics_master**: 0 not in roster (none); 2 roster participants missing (MIDL091; MIDL092).
- **redcap_ids_sr**: 0 not in roster (none); 5 roster participants missing (MIDL028; MIDL040; MIDL058; MIDL060; MIDL071).
- **ad_plasma**: 0 not in roster (none); 9 roster participants missing (MIDL018; MIDL021; MIDL028; MIDL029; MIDL040; MIDL058; MIDL060; MIDL091; MIDL092).
- **ad_csf**: 0 not in roster (none); 38 roster participants missing (MIDL003; MIDL006; MIDL008; MIDL011; MIDL014; MIDL016; MIDL018; MIDL021; MIDL022; MIDL025; MIDL028; MIDL029; MIDL031; MIDL032; MIDL037; MIDL040; MIDL042; MIDL044; MIDL047; MIDL049; MIDL050; MIDL051; MIDL052; MIDL055; MIDL058; MIDL060; MIDL062; MIDL066; MIDL071; MIDL073; MIDL077; MIDL086; MIDL087; MIDL088; MIDL089; MIDL090; MIDL091; MIDL092).
- **plasma_immune**: 0 not in roster (none); 9 roster participants missing (MIDL018; MIDL021; MIDL028; MIDL029; MIDL040; MIDL058; MIDL060; MIDL091; MIDL092).
- **csf_immune**: 0 not in roster (none); 38 roster participants missing (MIDL003; MIDL006; MIDL008; MIDL011; MIDL014; MIDL016; MIDL018; MIDL021; MIDL022; MIDL025; MIDL028; MIDL029; MIDL031; MIDL032; MIDL037; MIDL040; MIDL042; MIDL044; MIDL047; MIDL049; MIDL050; MIDL051; MIDL052; MIDL055; MIDL058; MIDL060; MIDL062; MIDL066; MIDL071; MIDL073; MIDL077; MIDL086; MIDL087; MIDL088; MIDL089; MIDL090; MIDL091; MIDL092).
- **metabolic_markers**: 0 not in roster (none); 0 roster participants missing (none).
- **cantab_session**: 0 not in roster (none); 11 roster participants missing (MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL059; MIDL060; MIDL071; MIDL087; MIDL091; MIDL092).
- **mrs_acc**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **mrs_pcc**: 0 not in roster (none); 10 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL083; MIDL091).
- **mrs_l_basal**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **mrs_r_basal**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **lh_cortical_area**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **rh_cortical_area**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **lh_cortical_thickness**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **rh_cortical_thickness**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **lh_cortical_volume**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **rh_cortical_volume**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **subcortical_volume**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **hippo_lh**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **hippo_rh**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **amygdala_lh**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **amygdala_rh**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **thalamus_lh**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **thalamus_rh**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **xtract**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **dti_combined**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **dti_ctnfr2_20230406**: 0 not in roster (none); 9 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL058; MIDL060; MIDL071; MIDL091).
- **reho**: 0 not in roster (none); 11 roster participants missing (MIDL006; MIDL028; MIDL029; MIDL040; MIDL042; MIDL048; MIDL053; MIDL058; MIDL060; MIDL071; MIDL091).
`phenom`, checked against the roster source `phenom_with_metabolics` (72 participants):

- **phenom_master**: 9 not in roster (PHE015; PHE022; PHE026; PHE042; PHE052; PHE087; PHE090; PHE096; PHE109); 32 roster participants missing (PHE001; PHE002; PHE003; PHE004; PHE005; PHE006; PHE010; PHE011; PHE013; PHE017; PHE019; PHE025; PHE027; PHE028; PHE030; PHE031; PHE037; PHE040; PHE049; PHE054; PHE064; PHE070; PHE071; PHE079; PHE081; PHE082; PHE083; PHE084; PHE086; PHE092; PHE093; PHE095).
- **albumin**: 23 not in roster (PHE009; PHE022; PHE034; PHE036; PHE038; PHE045; PHE047; PHE050; PHE052; PHE053; PHE058; PHE062; PHE065; PHE066; PHE069; PHE073; PHE075; PHE078; PHE085; PHE087; PHE090; PHE096; PHE109); 0 roster participants missing (none).

## Duplicate keys

None.

## Conflicting values

39 cells differ between sources. The earlier source in the config was kept.

| table | subject_key | variable | kept_source | kept_value | other_source | other_value |
|---|---|---|---|---|---|---|
| combined | MIDL041 | dob | demographics_master | (withheld) | demographics | (withheld) |
| combined | MIDL007 | age | demographics_master | 55 | metabolic_markers | 54 |
| combined | MIDL011 | age | demographics_master | 59 | metabolic_markers | 60 |
| combined | MIDL031 | age | demographics_master | 38 | metabolic_markers | 37 |
| combined | MIDL034 | age | demographics_master | 57 | metabolic_markers | 52 |
| combined | MIDL041 | age | demographics_master | 62 | metabolic_markers | 63 |
| combined | MIDL070 | sex | demographics_master | 1 | cantab_session | 2 |
| combined | MIDL019 | group | demographics_master | 0 | cantab_session | 1 |
| phenom | PHE014 | hsCRP | phenom_with_metabolics | 0.4801 | phenom_master | 0.6249 |
| phenom | PHE020 | hsCRP | phenom_with_metabolics | 4.5127 | phenom_master | 7.79 |
| phenom | PHE035 | hsCRP | phenom_with_metabolics | 4.2943 | phenom_master | 6.29 |
| phenom | PHE039 | hsCRP | phenom_with_metabolics | 0.0571 | phenom_master | 0.12 |
| phenom | PHE041 | hsCRP | phenom_with_metabolics | 0.1473 | phenom_master | 0.32 |
| phenom | PHE051 | hsCRP | phenom_with_metabolics | 1.7633 | phenom_master | 2.34 |
| phenom | PHE055 | hsCRP | phenom_with_metabolics | 0.1144 | phenom_master | 0.14 |
| phenom | PHE056 | hsCRP | phenom_with_metabolics | 0.3681 | phenom_master | 0.59 |
| phenom | PHE059 | hsCRP | phenom_with_metabolics | 0.1556 | phenom_master | 0.02 |
| phenom | PHE063 | hsCRP | phenom_with_metabolics | 0.2728 | phenom_master | 0.33 |
| phenom | PHE067 | hsCRP | phenom_with_metabolics | 2.0745 | phenom_master | 2.72 |
| phenom | PHE072 | hsCRP | phenom_with_metabolics | 1.6315 | phenom_master | 2.71 |
| phenom | PHE074 | hsCRP | phenom_with_metabolics | 1.4556 | phenom_master | 2.357 |
| phenom | PHE076 | hsCRP | phenom_with_metabolics | 2.0838 | phenom_master | 2.88 |
| phenom | PHE077 | hsCRP | phenom_with_metabolics | 6.9351 | phenom_master | 10.31 |
| phenom | PHE088 | hsCRP | phenom_with_metabolics | 4.1602 | phenom_master | 6.02 |
| phenom | PHE089 | hsCRP | phenom_with_metabolics | 0.639 | phenom_master | 1.32 |
| phenom | PHE091 | hsCRP | phenom_with_metabolics | 2.9681 | phenom_master | 5.46 |
| phenom | PHE094 | hsCRP | phenom_with_metabolics | 0.0517 | phenom_master | 0.11 |
| phenom | PHE097 | hsCRP | phenom_with_metabolics | 2.2958 | phenom_master | 3.75 |
| phenom | PHE098 | hsCRP | phenom_with_metabolics | 0.3272 | phenom_master | 0.57 |
| phenom | PHE099 | hsCRP | phenom_with_metabolics | 3.3998 | phenom_master | 4.85 |
| phenom | PHE100 | hsCRP | phenom_with_metabolics | 1.9732 | phenom_master | 2.82 |
| phenom | PHE101 | hsCRP | phenom_with_metabolics | 0.02 | phenom_master | 0.097 |
| phenom | PHE102 | hsCRP | phenom_with_metabolics | 0.1254 | phenom_master | 0.24 |
| phenom | PHE103 | hsCRP | phenom_with_metabolics | 3.4527 | phenom_master | 5.05 |
| phenom | PHE104 | hsCRP | phenom_with_metabolics | 0.6256 | phenom_master | 1.3 |
| phenom | PHE105 | hsCRP | phenom_with_metabolics | 0.3447 | phenom_master | 0.86 |
| phenom | PHE106 | hsCRP | phenom_with_metabolics | 0.9945 | phenom_master | 1.44 |
| phenom | PHE108 | hsCRP | phenom_with_metabolics | 1.961 | phenom_master | 2.86 |
| phenom | PHE110 | hsCRP | phenom_with_metabolics | 0.1915 | phenom_master | 0.58 |

## Variables supplied by more than one source

brainsegvolnotvent; etiv; ethnicity; race; sex; bmi; occupation; education; work_status; income; relationship; age; group; dob; occupation_oth; smoker; falling_asleep_1; sleep_night_2; waking_up_3; sleep_too_much_4; feeling_sad_5; irritable_6; anxious_7; mood_good_8; mood_time_9; mood_time_9a; mood_time_9b; quality_mood_10; appetite; decreased_11; increased_12; last_2weeks_13; last_2weeks_14; decision_15; myself_16; future_17; death_18; general_19; energy_20; pleasure_21; … (110 more)
