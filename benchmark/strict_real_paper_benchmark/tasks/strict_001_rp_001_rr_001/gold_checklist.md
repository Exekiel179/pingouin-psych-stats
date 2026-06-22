# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_001_rp_001_rr_001/sources/data/Keller_et_al._2017_CRSP_Power_Poses_-_Raw_data.csv` (data, 96167 bytes)
- `tasks/strict_001_rp_001_rr_001/sources/script/Keller_et_al._2017_CRSP_Power_Poses_-_Analysis_script.R` (script, 57978 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: anova, correlation, regression, reliability
- Candidate variables: Gamble, aware, expansive, feelpower, mexpa_3, mhire_3, mperf_3, prior_aware

Snippets:

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

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
