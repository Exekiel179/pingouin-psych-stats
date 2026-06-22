You are completing a strict real-paper psychology benchmark task.

Paper: Weston 2018 registered report
Journal: Journal of Research in Personality
Paper URL/DOI: https://doi.org/10.1016/j.jrp.2017.10.005
Original repository: https://osf.io/hr7vx/

Local data files:
- tasks/strict_017_rp_029_rr_029/sources/data/SPI_Items_used.xlsx
- tasks/strict_017_rp_029_rr_029/sources/data/Neuroticism_26_Vigilance_-_Final_Version_August_21_2C_2017_12.21_skip23.csv

Local script files:
- tasks/strict_017_rp_029_rr_029/sources/script/extra_analyses.R
- tasks/strict_017_rp_029_rr_029/sources/script/vigilance.R

Local document/readme files:
- tasks/strict_017_rp_029_rr_029/sources/doc/SF_3_Measures.pdf
- tasks/strict_017_rp_029_rr_029/sources/doc/SF_1_Analyses.pdf
- tasks/strict_017_rp_029_rr_029/sources/doc/SF_2_Exploratory.pdf
- tasks/strict_017_rp_029_rr_029/sources/doc/Pre-registration_revised.pdf

Detected analysis families from scripts: anova, correlation, regression, mediation, reliability
Candidate variables from scripts: outcome, stat
Script analysis snippets:
- `(alpha.c <- psych::alpha(vigdata[, con.items], check.keys = T))`
- `c.keys <- alpha.c$keys`
- `(alpha.ax <- psych::alpha(vigdata[, anxiety.items], check.keys = T))`
- `ax.keys <- alpha.ax$keys`
- `(alpha.es <- psych::alpha(vigdata[, emotionalstability.items], check.keys = T))`
- `es.keys <- alpha.es$keys`
- `(alpha.in <- psych::alpha(vigdata[, industry.items], check.keys = T))`
- `in.keys <- alpha.in$keys*-1`
- `(alpha.ir <- psych::alpha(vigdata[, irritability.items], check.keys = T))`
- `ir.keys <- alpha.ir$keys*-1`
- `(alpha.or <- psych::alpha(vigdata[, order.items], check.keys = T))`
- `or.keys <- alpha.or$keys*-1`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
