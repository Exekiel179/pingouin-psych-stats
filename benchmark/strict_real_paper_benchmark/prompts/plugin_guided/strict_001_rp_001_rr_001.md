Use `$pingouin-stat` and `$pg-analysis-approval`.
Route to the smallest applicable Pingouin workflow. If the original script uses a method outside Pingouin scope, state that explicitly and give the closest safe Pingouin subset only if defensible.

You are completing a strict real-paper psychology benchmark task.

Paper: Keller 2017 registered report
Journal: Comprehensive Results in Social Psychology
Paper URL/DOI: https://doi.org/10.1080/23743603.2017.1341186
Original repository: https://osf.io/pke79/

Local data files:
- tasks/strict_001_rp_001_rr_001/sources/data/Keller_et_al._2017_CRSP_Power_Poses_-_Raw_data.csv

Local script files:
- tasks/strict_001_rp_001_rr_001/sources/script/Keller_et_al._2017_CRSP_Power_Poses_-_Analysis_script.R

Local document/readme files:
- none

Detected analysis families from scripts: anova, correlation, regression, reliability
Candidate variables from scripts: Gamble, aware, expansive, feelpower, mexpa_3, mhire_3, mperf_3, prior_aware
Script analysis snippets:
- `cor.test(df$powerful, df$in_charge) #r = .79`
- `alpha(df[, c("accomplished", "successful", "achieving", "fullfilled", "self.worth", "confident", "productive")])`
- `# alpha = .94`
- `# Factorial anova: awareness, pose, and their interaction predicting feelings of power`
- `mymodel <- lm(feelpower ~ aware * expansive, data = dfe)`
- `anovm <- anova(mymodel)`
- `# Factorial logistic regression: awareness, pose, and their interaction predicting the decision to role the die`
- `mylogit <- glm(Gamble ~ aware * expansive, family = binomial(link = "logit"), data = dfe)`
- `# Factorial anova: awareness, pose, and their interaction predicting performance ratings (bonferroni corrected alpha = .025)`
- `mymodel <- lm(mperf_3 ~ aware * expansive, data = dfe)`
- `# Factorial anova: awareness, pose, and their interaction predicting hireability ratings (bonferroni corrected alpha = .025)`
- `mymodel <- lm(mhire_3 ~ aware * expansive, data = dfe)`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
