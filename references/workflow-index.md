# Workflow Index

This is the compact routing index. For public entry points, command aliases, and loading boundaries, read `../MODE_REGISTRY.md` and `exposure-policy.md` first.

Use this file before loading the longer API quick reference.

## Fast Routing

| User intent | Skill | Pingouin functions |
| --- | --- | --- |
| run/resume the complete stateful workflow with archive and approval gates | `pg-workflow` | dispatches the stages below |
| end-to-end psychology analysis with intake, routing, approval, reporting | `pingouin-stat` | routes to selected functions |
| inspect dataset, missingness, assumptions, reshape, outliers | `pg-data-screening` | `normality`, `homoscedasticity`, `sphericity`, `madmedianrule`, `qqplot` |
| compare means between one/two/many conditions | `pg-mean-tests` | `ttest`, `pairwise_tests` |
| omnibus group/time/factor effects | `pg-anova` | `anova`, `welch_anova`, `rm_anova`, `mixed_anova`, `ancova` |
| associations between variables | `pg-correlations` | `corr`, `partial_corr`, `pairwise_corr`, `rm_corr` |
| prediction, binary outcome, mediation | `pg-regression-mediation` | `linear_regression`, `logistic_regression`, `mediation_analysis` |
| ordinal / non-normal outcomes, rank-based tests | `pg-nonparametric` | `mwu`, `wilcoxon`, `kruskal`, `friedman`, `cochran` |
| categorical variables, contingency tables, chi-square | `pg-categorical` | `chi2_independence`, `chi2_mcnemar`, `dichotomous_crosstab`, `power_chi2` |
| Bayes factors for t test, correlation, or proportion | `pg-bayesian` | `bayesfactor_ttest`, `bayesfactor_pearson`, `bayesfactor_binom` |
| several dependent variables together, Hotelling's T-squared | `pg-multivariate` | `multivariate_ttest`, `box_m`, `multivariate_normality` |
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
- Non-parametric: outcome (ordinal/non-normal), between or within factor, subject ID if repeated.
- Categorical: two categorical columns; independent (chi-square) vs paired dichotomous (McNemar).
- Bayesian: t value + group sizes, or r + n, or successes + trials; prior scale.
- Multivariate: two or more continuous DVs; grouping column for the two-sample test and Box's M.
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
