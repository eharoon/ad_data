# Merge QC report

Generated 2026-11-20 20:43 UTC by `scripts/build_combined.py`.

## Summary

- `combined.csv`: 92 rows, 92 participants and 1098 variables from 30 sources.
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
| phenom_master | merged | 49 | 49 | 49 |  |
| phenom_with_metabolics | merged | 72 | 72 | 72 |  |
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

208 cells differ between sources. The earlier source in the config was kept.

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
| phenom | PHE091 | CHOL | phenom_master | 97 | phenom_with_metabolics | 152 |
| phenom | PHE094 | CHOL | phenom_master | 123 | phenom_with_metabolics | 97 |
| phenom | PHE097 | CHOL | phenom_master | 126 | phenom_with_metabolics | 123 |
| phenom | PHE098 | CHOL | phenom_master | 145 | phenom_with_metabolics | 126 |
| phenom | PHE099 | CHOL | phenom_master | 116 | phenom_with_metabolics | 145 |
| phenom | PHE100 | CHOL | phenom_master | 130 | phenom_with_metabolics | 116 |
| phenom | PHE101 | CHOL | phenom_master | 197 | phenom_with_metabolics | 130 |
| phenom | PHE102 | CHOL | phenom_master | 153 | phenom_with_metabolics | 197 |
| phenom | PHE103 | CHOL | phenom_master | 116 | phenom_with_metabolics | 153 |
| phenom | PHE104 | CHOL | phenom_master | 127 | phenom_with_metabolics | 116 |
| phenom | PHE105 | CHOL | phenom_master | 132 | phenom_with_metabolics | 127 |
| phenom | PHE106 | CHOL | phenom_master | 159 | phenom_with_metabolics | 132 |
| phenom | PHE108 | CHOL | phenom_master | 167 | phenom_with_metabolics | 123 |
| phenom | PHE091 | TG | phenom_master | 57 | phenom_with_metabolics | 89 |
| phenom | PHE094 | TG | phenom_master | 46 | phenom_with_metabolics | 57 |
| phenom | PHE097 | TG | phenom_master | 42 | phenom_with_metabolics | 68 |
| phenom | PHE098 | TG | phenom_master | 221 | phenom_with_metabolics | 42 |
| phenom | PHE099 | TG | phenom_master | 82 | phenom_with_metabolics | 221 |
| phenom | PHE100 | TG | phenom_master | 48 | phenom_with_metabolics | 82 |
| phenom | PHE101 | TG | phenom_master | 86 | phenom_with_metabolics | 48 |
| phenom | PHE102 | TG | phenom_master | 55 | phenom_with_metabolics | 86 |
| phenom | PHE103 | TG | phenom_master | 50 | phenom_with_metabolics | 55 |
| phenom | PHE104 | TG | phenom_master | 103 | phenom_with_metabolics | 50 |
| phenom | PHE105 | TG | phenom_master | 41 | phenom_with_metabolics | 103 |
| phenom | PHE106 | TG | phenom_master | 75 | phenom_with_metabolics | 41 |
| phenom | PHE108 | TG | phenom_master | 56 | phenom_with_metabolics | 31 |
| phenom | PHE091 | HDLc | phenom_master | 30.6 | phenom_with_metabolics | 39.7 |
| phenom | PHE094 | HDLc | phenom_master | 49.4 | phenom_with_metabolics | 30.6 |
| phenom | PHE097 | HDLc | phenom_master | 52.2 | phenom_with_metabolics | 33 |
| phenom | PHE098 | HDLc | phenom_master | 32.2 | phenom_with_metabolics | 52.2 |
| phenom | PHE099 | HDLc | phenom_master | 23.7 | phenom_with_metabolics | 32.2 |
| phenom | PHE100 | HDLc | phenom_master | 56 | phenom_with_metabolics | 23.7 |
| phenom | PHE101 | HDLc | phenom_master | 39.8 | phenom_with_metabolics | 56 |
| phenom | PHE102 | HDLc | phenom_master | 44.9 | phenom_with_metabolics | 39.8 |
| phenom | PHE103 | HDLc | phenom_master | 46 | phenom_with_metabolics | 44.9 |
| phenom | PHE104 | HDLc | phenom_master | 37.2 | phenom_with_metabolics | 46 |
| phenom | PHE105 | HDLc | phenom_master | 55.1 | phenom_with_metabolics | 37.2 |
| phenom | PHE106 | HDLc | phenom_master | 30.6 | phenom_with_metabolics | 55.1 |
| phenom | PHE108 | HDLc | phenom_master | 39.7 | phenom_with_metabolics | 39.1 |
| phenom | PHE091 | LDLc | phenom_master | 61 | phenom_with_metabolics | 101 |
| phenom | PHE094 | LDLc | phenom_master | 69 | phenom_with_metabolics | 61 |
| phenom | PHE097 | LDLc | phenom_master | 66 | phenom_with_metabolics | 90 |
| phenom | PHE098 | LDLc | phenom_master | 87 | phenom_with_metabolics | 66 |
| phenom | PHE099 | LDLc | phenom_master | 92 | phenom_with_metabolics | 87 |
| phenom | PHE100 | LDLc | phenom_master | 64 | phenom_with_metabolics | 92 |
| phenom | PHE101 | LDLc | phenom_master | 142 | phenom_with_metabolics | 64 |
| phenom | PHE102 | LDLc | phenom_master | 98 | phenom_with_metabolics | 142 |
| phenom | PHE103 | LDLc | phenom_master | 65 | phenom_with_metabolics | 98 |
| phenom | PHE104 | LDLc | phenom_master | 77 | phenom_with_metabolics | 65 |
| phenom | PHE106 | LDLc | phenom_master | 129 | phenom_with_metabolics | 77 |
| phenom | PHE108 | LDLc | phenom_master | 121 | phenom_with_metabolics | 81 |
| phenom | PHE091 | non-HDLc | phenom_master | 66.4 | phenom_with_metabolics | 112.3 |
| phenom | PHE094 | non-HDLc | phenom_master | 73.6 | phenom_with_metabolics | 66.4 |
| phenom | PHE097 | non-HDLc | phenom_master | 73.8 | phenom_with_metabolics | 90 |
| phenom | PHE098 | non-HDLc | phenom_master | 112.8 | phenom_with_metabolics | 73.8 |
| phenom | PHE099 | non-HDLc | phenom_master | 92.3 | phenom_with_metabolics | 112.8 |
| phenom | PHE100 | non-HDLc | phenom_master | 74 | phenom_with_metabolics | 92.3 |
| phenom | PHE101 | non-HDLc | phenom_master | 157.2 | phenom_with_metabolics | 74 |
| phenom | PHE102 | non-HDLc | phenom_master | 108.1 | phenom_with_metabolics | 157.2 |
| phenom | PHE103 | non-HDLc | phenom_master | 70 | phenom_with_metabolics | 108.1 |
| phenom | PHE104 | non-HDLc | phenom_master | 89.8 | phenom_with_metabolics | 70 |
| phenom | PHE105 | non-HDLc | phenom_master | 76.9 | phenom_with_metabolics | 89.8 |
| phenom | PHE106 | non-HDLc | phenom_master | 128.4 | phenom_with_metabolics | 76.9 |
| phenom | PHE108 | non-HDLc | phenom_master | 127.3 | phenom_with_metabolics | 83.9 |
| phenom | PHE014 | hsCRP | phenom_master | 0.6249 | phenom_with_metabolics | 0.4801 |
| phenom | PHE020 | hsCRP | phenom_master | 7.79 | phenom_with_metabolics | 4.5127 |
| phenom | PHE035 | hsCRP | phenom_master | 6.29 | phenom_with_metabolics | 4.2943 |
| phenom | PHE039 | hsCRP | phenom_master | 0.12 | phenom_with_metabolics | 0.0571 |
| phenom | PHE041 | hsCRP | phenom_master | 0.32 | phenom_with_metabolics | 0.1473 |
| phenom | PHE051 | hsCRP | phenom_master | 2.34 | phenom_with_metabolics | 1.7633 |
| phenom | PHE055 | hsCRP | phenom_master | 0.14 | phenom_with_metabolics | 0.1144 |
| phenom | PHE056 | hsCRP | phenom_master | 0.59 | phenom_with_metabolics | 0.3681 |
| phenom | PHE059 | hsCRP | phenom_master | 0.02 | phenom_with_metabolics | 0.1556 |
| phenom | PHE063 | hsCRP | phenom_master | 0.33 | phenom_with_metabolics | 0.2728 |
| phenom | PHE067 | hsCRP | phenom_master | 2.72 | phenom_with_metabolics | 2.0745 |
| phenom | PHE072 | hsCRP | phenom_master | 2.71 | phenom_with_metabolics | 1.6315 |
| phenom | PHE074 | hsCRP | phenom_master | 2.357 | phenom_with_metabolics | 1.4556 |
| phenom | PHE076 | hsCRP | phenom_master | 2.88 | phenom_with_metabolics | 2.0838 |
| phenom | PHE077 | hsCRP | phenom_master | 10.31 | phenom_with_metabolics | 6.9351 |
| phenom | PHE088 | hsCRP | phenom_master | 6.02 | phenom_with_metabolics | 4.1602 |
| phenom | PHE089 | hsCRP | phenom_master | 1.32 | phenom_with_metabolics | 0.639 |
| phenom | PHE091 | hsCRP | phenom_master | 5.46 | phenom_with_metabolics | 2.9681 |
| phenom | PHE094 | hsCRP | phenom_master | 0.11 | phenom_with_metabolics | 0.0517 |
| phenom | PHE097 | hsCRP | phenom_master | 3.75 | phenom_with_metabolics | 2.2958 |
| phenom | PHE098 | hsCRP | phenom_master | 0.57 | phenom_with_metabolics | 0.3272 |
| phenom | PHE099 | hsCRP | phenom_master | 4.85 | phenom_with_metabolics | 3.3998 |
| phenom | PHE100 | hsCRP | phenom_master | 2.82 | phenom_with_metabolics | 1.9732 |
| phenom | PHE101 | hsCRP | phenom_master | 0.097 | phenom_with_metabolics | 0.02 |
| phenom | PHE102 | hsCRP | phenom_master | 0.24 | phenom_with_metabolics | 0.1254 |
| phenom | PHE103 | hsCRP | phenom_master | 5.05 | phenom_with_metabolics | 3.4527 |
| phenom | PHE104 | hsCRP | phenom_master | 1.3 | phenom_with_metabolics | 0.6256 |
| phenom | PHE105 | hsCRP | phenom_master | 0.86 | phenom_with_metabolics | 0.3447 |
| phenom | PHE106 | hsCRP | phenom_master | 1.44 | phenom_with_metabolics | 0.9945 |
| phenom | PHE108 | hsCRP | phenom_master | 2.86 | phenom_with_metabolics | 1.961 |
| phenom | PHE110 | hsCRP | phenom_master | 0.58 | phenom_with_metabolics | 0.1915 |
| phenom | PHE091 | INS | phenom_master | 20.9 | phenom_with_metabolics | 128.2 |
| phenom | PHE094 | INS | phenom_master | 15.4 | phenom_with_metabolics | 20.9 |
| phenom | PHE097 | INS | phenom_master | 57.9 | phenom_with_metabolics | 30.1 |
| phenom | PHE098 | INS | phenom_master | 117.4 | phenom_with_metabolics | 57.9 |
| phenom | PHE099 | INS | phenom_master | 100.7 | phenom_with_metabolics | 117.4 |
| phenom | PHE100 | INS | phenom_master | 41.2 | phenom_with_metabolics | 100.7 |
| phenom | PHE101 | INS | phenom_master | 24.8 | phenom_with_metabolics | 41.2 |
| phenom | PHE102 | INS | phenom_master | 73.5 | phenom_with_metabolics | 24.8 |
| phenom | PHE103 | INS | phenom_master | 42.4 | phenom_with_metabolics | 73.5 |
| phenom | PHE104 | INS | phenom_master | 51 | phenom_with_metabolics | 42.4 |
| phenom | PHE105 | INS | phenom_master | 13.7 | phenom_with_metabolics | 51 |
| phenom | PHE106 | INS | phenom_master | 84.2 | phenom_with_metabolics | 13.7 |
| phenom | PHE108 | INS | phenom_master | 49.7 | phenom_with_metabolics | 40.4 |
| phenom | PHE091 | GLU | phenom_master | 116.7 | phenom_with_metabolics | 85.5 |
| phenom | PHE094 | GLU | phenom_master | 121 | phenom_with_metabolics | 116.7 |
| phenom | PHE097 | GLU | phenom_master | 113.9 | phenom_with_metabolics | 104.7 |
| phenom | PHE098 | GLU | phenom_master | 108.8 | phenom_with_metabolics | 113.9 |
| phenom | PHE099 | GLU | phenom_master | 102.8 | phenom_with_metabolics | 108.8 |
| phenom | PHE100 | GLU | phenom_master | 144.9 | phenom_with_metabolics | 102.8 |
| phenom | PHE101 | GLU | phenom_master | 96.8 | phenom_with_metabolics | 144.9 |
| phenom | PHE102 | GLU | phenom_master | 102.1 | phenom_with_metabolics | 96.8 |
| phenom | PHE103 | GLU | phenom_master | 129.1 | phenom_with_metabolics | 102.1 |
| phenom | PHE104 | GLU | phenom_master | 91.7 | phenom_with_metabolics | 129.1 |
| phenom | PHE105 | GLU | phenom_master | 111.7 | phenom_with_metabolics | 91.7 |
| phenom | PHE106 | GLU | phenom_master | 97.5 | phenom_with_metabolics | 111.7 |
| phenom | PHE108 | GLU | phenom_master | 96.4 | phenom_with_metabolics | 90.3 |
| phenom | PHE091 | NEFA | phenom_master | 0.22 | phenom_with_metabolics | 0.21 |
| phenom | PHE094 | NEFA | phenom_master | 0.18 | phenom_with_metabolics | 0.22 |
| phenom | PHE097 | NEFA | phenom_master | 1.95 | phenom_with_metabolics | 2.3 |
| phenom | PHE098 | NEFA | phenom_master | 2.88 | phenom_with_metabolics | 1.95 |
| phenom | PHE099 | NEFA | phenom_master | 0.36 | phenom_with_metabolics | 2.88 |
| phenom | PHE100 | NEFA | phenom_master | 0.16 | phenom_with_metabolics | 0.36 |
| phenom | PHE101 | NEFA | phenom_master | 0.24 | phenom_with_metabolics | 0.16 |
| phenom | PHE102 | NEFA | phenom_master | 0.14 | phenom_with_metabolics | 0.24 |
| phenom | PHE103 | NEFA | phenom_master | 0.29 | phenom_with_metabolics | 0.14 |
| phenom | PHE104 | NEFA | phenom_master | 0.22 | phenom_with_metabolics | 0.29 |
| phenom | PHE105 | NEFA | phenom_master | 0.11 | phenom_with_metabolics | 0.22 |
| phenom | PHE106 | NEFA | phenom_master | 2.59 | phenom_with_metabolics | 0.11 |
| phenom | PHE108 | NEFA | phenom_master | 0.16 | phenom_with_metabolics | 2.05 |
| phenom | PHE091 | FolicAcid | phenom_master | 1540.7638157253828 | phenom_with_metabolics | 2113.81849 |
| phenom | PHE094 | FolicAcid | phenom_master | 1893.7881461850288 | phenom_with_metabolics | 1540.763816 |
| phenom | PHE097 | FolicAcid | phenom_master | 1489.5664248709822 | phenom_with_metabolics | 2035.412052 |
| phenom | PHE098 | FolicAcid | phenom_master | 2046.9682334075555 | phenom_with_metabolics | 1489.566425 |
| phenom | PHE099 | FolicAcid | phenom_master | 1849.8019808472973 | phenom_with_metabolics | 2046.968233 |
| phenom | PHE100 | FolicAcid | phenom_master | 2507.188182627962 | phenom_with_metabolics | 1849.801981 |
| phenom | PHE101 | FolicAcid | phenom_master | 2056.253220306374 | phenom_with_metabolics | 2507.188183 |
| phenom | PHE102 | FolicAcid | phenom_master | 2277.939966492307 | phenom_with_metabolics | 2056.25322 |
| phenom | PHE103 | FolicAcid | phenom_master | 1416.1929844062677 | phenom_with_metabolics | 2277.939966 |
| phenom | PHE104 | FolicAcid | phenom_master | 1880.1915711312397 | phenom_with_metabolics | 1416.192984 |
| phenom | PHE105 | FolicAcid | phenom_master | 1914.353435812324 | phenom_with_metabolics | 1880.191571 |
| phenom | PHE106 | FolicAcid | phenom_master | 1540.4498904393686 | phenom_with_metabolics | 1914.353436 |
| phenom | PHE108 | FolicAcid | phenom_master | 2057.3470145148867 | phenom_with_metabolics | 1814.47665 |
| phenom | PHE091 | Adiponectin | phenom_master | 2210.267911321512 | phenom_with_metabolics | 1030.025 |
| phenom | PHE094 | Adiponectin | phenom_master | 1715.4848837129139 | phenom_with_metabolics | 2210.267911 |
| phenom | PHE097 | Adiponectin | phenom_master | 1095.8368790888512 | phenom_with_metabolics | 1680.291992 |
| phenom | PHE098 | Adiponectin | phenom_master | 819.7170764888581 | phenom_with_metabolics | 1095.836879 |
| phenom | PHE099 | Adiponectin | phenom_master | 846.4676706770613 | phenom_with_metabolics | 819.7170765 |
| phenom | PHE100 | Adiponectin | phenom_master | 964.3781181722543 | phenom_with_metabolics | 846.4676707 |
| phenom | PHE101 | Adiponectin | phenom_master | 2489.447000343387 | phenom_with_metabolics | 964.3781182 |
| phenom | PHE102 | Adiponectin | phenom_master | 1742.3878396512646 | phenom_with_metabolics | 2489.447 |
| phenom | PHE103 | Adiponectin | phenom_master | 1789.1673828110238 | phenom_with_metabolics | 1742.38784 |
| phenom | PHE104 | Adiponectin | phenom_master | 1552.554399195301 | phenom_with_metabolics | 1789.167383 |
| phenom | PHE105 | Adiponectin | phenom_master | 1948.5107356347412 | phenom_with_metabolics | 1552.554399 |
| phenom | PHE106 | Adiponectin | phenom_master | 760.6747423171571 | phenom_with_metabolics | 1948.510736 |
| phenom | PHE108 | Adiponectin | phenom_master | 1277.3327876676058 | phenom_with_metabolics | 1025.705511 |
| phenom | PHE091 | Leptin | phenom_master | 3604.224814489984 | phenom_with_metabolics | 18410.86873 |
| phenom | PHE094 | Leptin | phenom_master | 17886.29084404285 | phenom_with_metabolics | 3604.224814 |
| phenom | PHE097 | Leptin | phenom_master | 18098.23882317501 | phenom_with_metabolics | 18151.27868 |
| phenom | PHE098 | Leptin | phenom_master | 12712.669896283642 | phenom_with_metabolics | 18098.23882 |
| phenom | PHE099 | Leptin | phenom_master | 14260.895321343316 | phenom_with_metabolics | 12712.6699 |
| phenom | PHE100 | Leptin | phenom_master | 12337.63266950062 | phenom_with_metabolics | 14260.89532 |
| phenom | PHE101 | Leptin | phenom_master | 18062.90617712574 | phenom_with_metabolics | 12337.63267 |
| phenom | PHE102 | Leptin | phenom_master | 18322.312980547424 | phenom_with_metabolics | 18062.90618 |
| phenom | PHE103 | Leptin | phenom_master | 18133.596253050455 | phenom_with_metabolics | 18322.31298 |
| phenom | PHE104 | Leptin | phenom_master | 16837.43568650917 | phenom_with_metabolics | 18133.59625 |
| phenom | PHE105 | Leptin | phenom_master | 17962.792858364133 | phenom_with_metabolics | 16837.43569 |
| phenom | PHE106 | Leptin | phenom_master | 8030.096442881836 | phenom_with_metabolics | 17962.79286 |
| phenom | PHE108 | Leptin | phenom_master | 18210.2317770997 | phenom_with_metabolics | 18239.71893 |
| phenom | PHE091 | Osteopontin | phenom_master | 32756.379807321955 | phenom_with_metabolics | 6500.006426 |
| phenom | PHE094 | Osteopontin | phenom_master | 827.8599808023087 | phenom_with_metabolics | 32756.37981 |
| phenom | PHE097 | Osteopontin | phenom_master | 11782.92310956951 | phenom_with_metabolics | 9058.931161 |
| phenom | PHE098 | Osteopontin | phenom_master | 10734.536861064753 | phenom_with_metabolics | 11782.92311 |
| phenom | PHE099 | Osteopontin | phenom_master | 32515.94148117103 | phenom_with_metabolics | 10734.53686 |
| phenom | PHE100 | Osteopontin | phenom_master | 7748.893961962905 | phenom_with_metabolics | 32515.94148 |
| phenom | PHE101 | Osteopontin | phenom_master | 7333.12600137612 | phenom_with_metabolics | 7748.893962 |
| phenom | PHE102 | Osteopontin | phenom_master | 14523.34462569898 | phenom_with_metabolics | 7333.126 |
| phenom | PHE103 | Osteopontin | phenom_master | 6155.110358839551 | phenom_with_metabolics | 14523.34463 |
| phenom | PHE104 | Osteopontin | phenom_master | 409.10407957979055 | phenom_with_metabolics | 6155.110359 |
| phenom | PHE105 | Osteopontin | phenom_master | 542.922269766222 | phenom_with_metabolics | 409.1040796 |
| phenom | PHE106 | Osteopontin | phenom_master | 7191.177123362225 | phenom_with_metabolics | 542.922 |
| phenom | PHE108 | Osteopontin | phenom_master | 4033.6585755789015 | phenom_with_metabolics | 14329.21992 |
| phenom | PHE051 | Resistin | phenom_master | 7.08031059198202 | phenom_with_metabolics | 7.080 |
| phenom | PHE091 | Resistin | phenom_master | 1160.2551579795459 | phenom_with_metabolics | 583.9092055 |
| phenom | PHE094 | Resistin | phenom_master | 1293.9964845770412 | phenom_with_metabolics | 1160.255158 |
| phenom | PHE097 | Resistin | phenom_master | 1403.9536320195486 | phenom_with_metabolics | 4342.671396 |
| phenom | PHE098 | Resistin | phenom_master | 5716.1827899416185 | phenom_with_metabolics | 1403.953632 |
| phenom | PHE099 | Resistin | phenom_master | 2751.4031354111953 | phenom_with_metabolics | 5716.18279 |

8 more conflicts are in the output folder's conflicts.csv.

## Variables supplied by more than one source

brainsegvolnotvent; etiv; ethnicity; race; sex; bmi; occupation; education; work_status; income; relationship; age; group; INS; GLU; Leptin; dob; occupation_oth; smoker; falling_asleep_1; sleep_night_2; waking_up_3; sleep_too_much_4; feeling_sad_5; irritable_6; anxious_7; mood_good_8; mood_time_9; mood_time_9a; mood_time_9b; quality_mood_10; appetite; decreased_11; increased_12; last_2weeks_13; last_2weeks_14; decision_15; myself_16; future_17; death_18; … (120 more)
