Use `$pingouin-stat` and `$pg-analysis-approval`.
Route to the smallest applicable Pingouin workflow. If the original script uses a method outside Pingouin scope, state that explicitly and give the closest safe Pingouin subset only if defensible.

You are completing a strict real-paper psychology benchmark task.

Paper: McCarthy 2017 registered report
Journal: Comprehensive Results in Social Psychology
Paper URL/DOI: https://doi.org/10.1080/23743603.2017.1378071
Original repository: https://osf.io/ptmn6/

Local data files:
- tasks/strict_002_rp_002_rr_002/sources/data/heat-aggression_AMP_pilot_data.csv
- tasks/strict_002_rp_002_rr_002/sources/data/heat-aggression_AMP_data.csv

Local script files:
- tasks/strict_002_rp_002_rr_002/sources/script/Heat-Aggression_AMP_Final_ms.Rmd
- tasks/strict_002_rp_002_rr_002/sources/script/heat-aggression_AMP.R
- tasks/strict_002_rp_002_rr_002/sources/script/heat-aggression_AMP_power_analysis.R
- tasks/strict_002_rp_002_rr_002/sources/script/Heat-Aggression_AMP_Power_Analysis.R
- tasks/strict_002_rp_002_rr_002/sources/script/heat-aggression_AMP_pilot.R
- tasks/strict_002_rp_002_rr_002/sources/script/Heat-Aggression_AMP_Pre-registration.R
- tasks/strict_002_rp_002_rr_002/sources/script/Heat-Aggression_AMP-predata-IPA_ms.Rmd

Local document/readme files:
- tasks/strict_002_rp_002_rr_002/sources/doc/Heat-Aggression_AMP_Pilot_Study_Preregistration.pdf

Detected analysis families from scripts: anova
Candidate variables from scripts: ampRating, ampTrial, ampTrialDummy, perceived.prime
Script analysis snippets:
- `anova(trialType, trialTypePrime)`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
