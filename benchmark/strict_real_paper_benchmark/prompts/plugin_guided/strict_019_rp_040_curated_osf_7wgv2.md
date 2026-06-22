Use `$pingouin-stat` and `$pg-analysis-approval`.
Route to the smallest applicable Pingouin workflow. If the original script uses a method outside Pingouin scope, state that explicitly and give the closest safe Pingouin subset only if defensible.

You are completing a strict real-paper psychology benchmark task.

Paper: Robustness report: Arechar et al. (2023), Nature Human Behaviour
Journal: Nature Human Behaviour
Paper URL/DOI: not recorded
Original repository: https://osf.io/7wgv2/

Local data files:
- tasks/strict_019_rp_040_curated_osf_7wgv2/sources/data/CR.csv
- tasks/strict_019_rp_040_curated_osf_7wgv2/sources/data/CR.csv

Local script files:
- tasks/strict_019_rp_040_curated_osf_7wgv2/sources/script/REP_supps-rev.Rmd
- tasks/strict_019_rp_040_curated_osf_7wgv2/sources/script/Fig1-rev2.R
- tasks/strict_019_rp_040_curated_osf_7wgv2/sources/script/REP_supps.Rmd

Local document/readme files:
- tasks/strict_019_rp_040_curated_osf_7wgv2/sources/doc/Fig1-rev2.pdf
- tasks/strict_019_rp_040_curated_osf_7wgv2/sources/doc/Fig1-rev.pdf
- tasks/strict_019_rp_040_curated_osf_7wgv2/sources/doc/REP_supps-rev.pdf
- tasks/strict_019_rp_040_curated_osf_7wgv2/sources/doc/REP_supps.pdf
- tasks/strict_019_rp_040_curated_osf_7wgv2/sources/doc/Fig1.pdf

Detected analysis families from scripts: reliability
Candidate variables from scripts: Condition, Country, Truth, value
Script analysis snippets:
- `ggdist::stat_halfeye(alpha = 0.7) + ylab(NULL) + theme_bw() +`
- `size = 6, alpha = 0.8) +`
- `width = 0.15, alpha = 0.8) +`
- `alpha = 0.8,`
- `boxplot.args = list(color = "black", outlier.shape = NA, show_guide = FALSE, alpha = 0.8),`
- `violin.args = list(color = "black", outlier.shape = NA, alpha = 0.7),`
- `point.args = list(show_guide = FALSE, alpha = 0)`
- `show_guide = FALSE, alpha = 0.8,`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
