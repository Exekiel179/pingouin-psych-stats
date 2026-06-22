Use `$pingouin-stat` and `$pg-analysis-approval`.
Route to the smallest applicable Pingouin workflow. If the original script uses a method outside Pingouin scope, state that explicitly and give the closest safe Pingouin subset only if defensible.

You are completing a strict real-paper psychology benchmark task.

Paper: Jackson 2017 registered report
Journal: Comprehensive Results in Social Psychology
Paper URL/DOI: https://doi.org/10.1080/23743603.2017.1341178
Original repository: https://osf.io/g85ep/?view_only=a4bc9c796ae347b08c4188251cebfe85

Local data files:
- tasks/strict_005_rp_005_rr_005/sources/data/2_-_Study_2_Pilot_dataset.sav
- tasks/strict_005_rp_005_rr_005/sources/data/4_-_Study_2_-_All_variables_dataset_N_128.csv
- tasks/strict_005_rp_005_rr_005/sources/data/2_-_Study_2_Pilot_dataset.csv
- tasks/strict_005_rp_005_rr_005/sources/data/3_-_Study_2_-_Raw_dataset_N_133.csv
- tasks/strict_005_rp_005_rr_005/sources/data/3_-_Study_2_-_Raw_dataset_N_133.sav
- tasks/strict_005_rp_005_rr_005/sources/data/5_-_Study_2_-_For_analyses_dataset_N_128.sav
- tasks/strict_005_rp_005_rr_005/sources/data/4_-_Study_2_-_All_variables_dataset_N_128_1.sav
- tasks/strict_005_rp_005_rr_005/sources/data/1_-_Study_1_dataset_N_65.sav
- tasks/strict_005_rp_005_rr_005/sources/data/5_-_Study_2_-_For_analyses_N_128.csv

Local script files:
- tasks/strict_005_rp_005_rr_005/sources/script/3_-_Additional_Analyses_for_Var_Creation.sps
- tasks/strict_005_rp_005_rr_005/sources/script/2_-_Additional_Analyses_for_Study_1.sps
- tasks/strict_005_rp_005_rr_005/sources/script/1_-_Analysis_Pipeline_for_CRSP.sps
- tasks/strict_005_rp_005_rr_005/sources/script/5_-_Additional_Analyses_Study_2.sps
- tasks/strict_005_rp_005_rr_005/sources/script/4_-_Additional_Analyses_for_Study_2_Pilot.sps

Local document/readme files:
- tasks/strict_005_rp_005_rr_005/sources/doc/SPSS_Dataset_Syntax_Guide.pdf

Detected analysis families from scripts: anova, correlation, regression, reliability
Candidate variables from scripts: not extracted
Script analysis snippets:
- `/CRITERIA=ALPHA(.05)`
- `/CRITERIA=ALPHA(0.05)`
- `* self-objectification using hierarchical linear regression`
- `REGRESSION`
- `/DESCRIPTIVES MEAN STDDEV CORR SIG N`
- `/STATISTICS COEFF OUTS CI(95) R ANOVA CHANGE`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
