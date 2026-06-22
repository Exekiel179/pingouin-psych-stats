Use `$pingouin-stat` and `$pg-analysis-approval`.
Route to the smallest applicable Pingouin workflow. If the original script uses a method outside Pingouin scope, state that explicitly and give the closest safe Pingouin subset only if defensible.

You are completing a strict real-paper psychology benchmark task.

Paper: Dwyer 2017 registered report
Journal: Comprehensive Results in Social Psychology
Paper URL/DOI: https://doi.org/10.1080/23743603.2017.1376580
Original repository: https://osf.io/23fd7/

Local data files:
- tasks/strict_004_rp_004_rr_004/sources/data/HvM_Study_1_Data_2017-07-06.csv

Local script files:
- tasks/strict_004_rp_004_rr_004/sources/script/HvM_Study_1_Syntax.sps

Local document/readme files:
- tasks/strict_004_rp_004_rr_004/sources/doc/MvH_S1_Survey.pdf
- tasks/strict_004_rp_004_rr_004/sources/doc/MvH_S1_Survey_Coded.pdf

Detected analysis families from scripts: anova, reliability
Candidate variables from scripts: not extracted
Script analysis snippets:
- `/CRITERIA=ALPHA(.05)`
- `*2-way ANOVA`
- `/CRITERIA=ALPHA(0.05)`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
