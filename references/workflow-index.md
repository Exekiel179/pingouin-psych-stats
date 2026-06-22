# Workflow Index

Use this file before loading the longer API quick reference.

## Fast Routing

| User intent | Skill | Pingouin functions |
| --- | --- | --- |
| end-to-end psychology analysis with intake, routing, approval, reporting | `pingouin-stat` | routes to selected functions |
| inspect dataset, missingness, assumptions, reshape | `pg-data-screening` | `normality`, `homoscedasticity`, `sphericity` |
| compare means between one/two/many conditions | `pg-mean-tests` | `ttest`, `pairwise_tests` |
| omnibus group/time/factor effects | `pg-anova` | `anova`, `welch_anova`, `rm_anova`, `mixed_anova`, `ancova` |
| associations between variables | `pg-correlations` | `corr`, `partial_corr`, `pairwise_corr`, `rm_corr` |
| prediction, binary outcome, mediation | `pg-regression-mediation` | `linear_regression`, `logistic_regression`, `mediation_analysis` |
| internal consistency or rater reliability | `pg-reliability` | `cronbach_alpha`, `intraclass_corr` |
| sample size or detectable effect | `pg-power` | `power_ttest`, `power_ttest2n`, `power_anova`, `power_rm_anova`, `power_corr` |
| result prose or tables | `pg-reporting` | `print_table` plus existing result objects |
| approve/check analysis before final interpretation | `pg-analysis-approval` | reviews selected functions and output |

## Minimum Inputs

- Mean tests: outcome, group/condition, paired status, subject ID if paired/repeated.
- ANOVA: outcome, between factor(s), within factor(s), subject ID for repeated/mixed designs.
- Correlation: variable pair(s), independence/repeated structure, covariates if partial.
- Regression: outcome scale, predictors, covariates, missing-data rule.
- Mediation: `x`, `m`, `y`, covariates, bootstrap count, seed.
- Reliability: item columns for alpha; target/rater/rating columns for ICC.
- Power: test family, effect size, alpha, target power, groups/measurements.
- Deliverable: output format, language, figure/table requirements, reporting standard.

## Stop Conditions

Ask a clarifying question instead of writing code when:

- The unit of analysis is ambiguous.
- Repeated measures or clustering might exist.
- The outcome scale does not match the requested test.
- Required columns are not named.
- Output format or figure/table requirement is required but unspecified.
- The user asks for causal interpretation from non-causal data.
