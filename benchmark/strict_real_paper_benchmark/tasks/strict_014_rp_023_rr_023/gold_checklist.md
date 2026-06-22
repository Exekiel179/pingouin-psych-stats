# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_014_rp_023_rr_023/sources/doc/Brindley_et_al._-_Laboratory_Log.pdf` (doc, 68876 bytes)
- `tasks/strict_014_rp_023_rr_023/sources/doc/Brindley_et_al._-_Supplemental_Material.pdf` (doc, 2138038 bytes)
- `tasks/strict_014_rp_023_rr_023/sources/data/Study_2_Data_SPSS_-_Public.sav` (data, 569127 bytes)
- `tasks/strict_014_rp_023_rr_023/sources/data/Study_2_Data_CSV_-_Public.csv` (data, 742813 bytes)
- `tasks/strict_014_rp_023_rr_023/sources/data/Study_2_-_Deidentified_Raw_Data.csv` (data, 341452 bytes)
- `tasks/strict_014_rp_023_rr_023/sources/data/Study_2_Codebook_-_Public.xlsx` (data, 15902 bytes)
- `tasks/strict_014_rp_023_rr_023/sources/script/Study_2_SPSS_Syntax_-_Public.sps` (script, 12780 bytes)
- `tasks/strict_014_rp_023_rr_023/sources/data/Study_1_Data_SPSS_-_Public.sav` (data, 587296 bytes)
- `tasks/strict_014_rp_023_rr_023/sources/data/Study_1_Data_CSV_-_Public.csv` (data, 754425 bytes)
- `tasks/strict_014_rp_023_rr_023/sources/data/Study_1_-_Deidentified_Raw_Data.csv` (data, 348657 bytes)
- `tasks/strict_014_rp_023_rr_023/sources/data/Study_1_Codebook_-_Public.xlsx` (data, 15987 bytes)
- `tasks/strict_014_rp_023_rr_023/sources/script/Study_1_SPSS_Syntax_-_Public.sps` (script, 12627 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: anova, correlation, regression, reliability
- Candidate variables: not extracted

Snippets:

- `/SCALE (ALPHA)=ALL/MODEL =ALPHA`
- `/SUMMARY=TOTAL MEANS CORR .`
- `/SCALE(ALPHA)=ALL/MODEL=ALPHA`
- `/SUMMARY=TOTAL MEANS CORR.`
- `*Regression Analyses*`
- `**Centered Regression Analysis**`
- `*Full Regression Model with all predictors - 4 and 5-way interactions are all n.s. so they are subsequently dropped from the model`
- `REGRESSION`
- `/STATISTICS COEFF OUTS CI(95) R ANOVA`
- `/MODEL=ALPHA.`

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
