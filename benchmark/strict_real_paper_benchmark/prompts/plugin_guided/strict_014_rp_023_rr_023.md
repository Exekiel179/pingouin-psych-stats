Use `$pingouin-stat` and `$pg-analysis-approval`.
Route to the smallest applicable Pingouin workflow. If the original script uses a method outside Pingouin scope, state that explicitly and give the closest safe Pingouin subset only if defensible.

You are completing a strict real-paper psychology benchmark task.

Paper: Brindley 2018 registered report
Journal: Comprehensive Results in Social Psychology
Paper URL/DOI: https://doi.org/10.1080/23743603.2018.1436939
Original repository: https://osf.io/6bwmq/

Local data files:
- tasks/strict_014_rp_023_rr_023/sources/data/Study_2_Data_SPSS_-_Public.sav
- tasks/strict_014_rp_023_rr_023/sources/data/Study_2_Data_CSV_-_Public.csv
- tasks/strict_014_rp_023_rr_023/sources/data/Study_2_-_Deidentified_Raw_Data.csv
- tasks/strict_014_rp_023_rr_023/sources/data/Study_2_Codebook_-_Public.xlsx
- tasks/strict_014_rp_023_rr_023/sources/data/Study_1_Data_SPSS_-_Public.sav
- tasks/strict_014_rp_023_rr_023/sources/data/Study_1_Data_CSV_-_Public.csv
- tasks/strict_014_rp_023_rr_023/sources/data/Study_1_-_Deidentified_Raw_Data.csv
- tasks/strict_014_rp_023_rr_023/sources/data/Study_1_Codebook_-_Public.xlsx

Local script files:
- tasks/strict_014_rp_023_rr_023/sources/script/Study_2_SPSS_Syntax_-_Public.sps
- tasks/strict_014_rp_023_rr_023/sources/script/Study_1_SPSS_Syntax_-_Public.sps

Local document/readme files:
- tasks/strict_014_rp_023_rr_023/sources/doc/Brindley_et_al._-_Laboratory_Log.pdf
- tasks/strict_014_rp_023_rr_023/sources/doc/Brindley_et_al._-_Supplemental_Material.pdf

Detected analysis families from scripts: anova, correlation, regression, reliability
Candidate variables from scripts: not extracted
Script analysis snippets:
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

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
