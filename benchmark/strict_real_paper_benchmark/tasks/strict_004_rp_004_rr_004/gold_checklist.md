# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_004_rp_004_rr_004/sources/script/HvM_Study_1_Syntax.sps` (script, 7236 bytes)
- `tasks/strict_004_rp_004_rr_004/sources/doc/MvH_S1_Survey.pdf` (doc, 196124 bytes)
- `tasks/strict_004_rp_004_rr_004/sources/doc/MvH_S1_Survey_Coded.pdf` (doc, 106362 bytes)
- `tasks/strict_004_rp_004_rr_004/sources/data/HvM_Study_1_Data_2017-07-06.csv` (data, 122811 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: anova, reliability
- Candidate variables: not extracted

Snippets:

- `/CRITERIA=ALPHA(.05)`
- `*2-way ANOVA`
- `/CRITERIA=ALPHA(0.05)`

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
