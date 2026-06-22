# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_005_rp_005_rr_005/sources/script/3_-_Additional_Analyses_for_Var_Creation.sps` (script, 24552 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/script/2_-_Additional_Analyses_for_Study_1.sps` (script, 2883 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/script/1_-_Analysis_Pipeline_for_CRSP.sps` (script, 12159 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/script/5_-_Additional_Analyses_Study_2.sps` (script, 6612 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/script/4_-_Additional_Analyses_for_Study_2_Pilot.sps` (script, 1503 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/data/2_-_Study_2_Pilot_dataset.sav` (data, 3073 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/data/4_-_Study_2_-_All_variables_dataset_N_128.csv` (data, 307323 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/data/2_-_Study_2_Pilot_dataset.csv` (data, 618 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/data/3_-_Study_2_-_Raw_dataset_N_133.csv` (data, 268620 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/data/3_-_Study_2_-_Raw_dataset_N_133.sav` (data, 418612 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/data/5_-_Study_2_-_For_analyses_dataset_N_128.sav` (data, 28070 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/data/4_-_Study_2_-_All_variables_dataset_N_128_1.sav` (data, 440809 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/data/1_-_Study_1_dataset_N_65.sav` (data, 255385 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/data/5_-_Study_2_-_For_analyses_N_128.csv` (data, 26751 bytes)
- `tasks/strict_005_rp_005_rr_005/sources/doc/SPSS_Dataset_Syntax_Guide.pdf` (doc, 101618 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: anova, correlation, regression, reliability
- Candidate variables: not extracted

Snippets:

- `/CRITERIA=ALPHA(.05)`
- `/CRITERIA=ALPHA(0.05)`
- `* self-objectification using hierarchical linear regression`
- `REGRESSION`
- `/DESCRIPTIVES MEAN STDDEV CORR SIG N`
- `/STATISTICS COEFF OUTS CI(95) R ANOVA CHANGE`

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
