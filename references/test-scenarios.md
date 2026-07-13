# Test Scenarios

Use these prompts to forward-test routing and supervision without leaking expected answers to an evaluator. The expected skill is listed here for maintainers; do not include it when asking another agent to solve the prompt.

| Prompt | Expected skill | Gate focus |
| --- | --- | --- |
| pingouin-stat: I need a full psychology analysis and final report, but I have not specified output format. | `pingouin-stat` | intake asks deliverable/method/data questions |
| I have pre/post anxiety scores from the same participants. Which test and code? | `pg-mean-tests` | S0 dependency, S1 subject pairing |
| Compare three therapy groups on post-treatment depression. | `pg-anova` | S0 between factor, S3 homogeneity |
| I measured mood at baseline, week 4, week 8 in treatment and control groups. | `pg-anova` | S0 mixed design, S1 subject ID, S3 sphericity |
| Is stress related to sleep quality after controlling age and baseline depression? | `pg-correlations` | S0 covariates, S5 non-causal |
| Predict dropout yes/no from motivation and age. | `pg-regression-mediation` | S0 binary outcome, S2 logistic signature |
| Does self-efficacy mediate intervention effects on wellbeing? | `pg-regression-mediation` | S0 path variables, S5 causal caveat |
| Compare two groups on a skewed reaction-time score with small n. | `pg-nonparametric` | S3 non-normal, rank-based test |
| Is therapy type associated with relapse (yes/no)? | `pg-categorical` | S0 R x C, chi-square, Cramér's V |
| Did symptom presence change from pre to post in the same patients? | `pg-categorical` | S0 paired binary, McNemar |
| How strong is the Bayesian evidence for the group difference? | `pg-bayesian` | S4 BF10, prior scale |
| Estimate reliability for a six-item resilience scale. | `pg-reliability` | S1 item columns, S5 alpha caveat |
| Three clinicians rated the same interviews; compute inter-rater reliability. | `pg-reliability` | S0 ICC model, S1 target-rater pairs |
| How many participants do I need for r = .30, 80% power? | `pg-power` | S0 alpha/power defaults |
| Convert this Pingouin ANOVA table into Chinese APA results. | `pg-reporting` | S4 output-derived prose |
| Review this analysis plan before I report it: independent t test on repeated pre/post rows. | `pg-analysis-approval` | catches ignored dependency |
| I uploaded data but do not know whether it is long or wide. | `pg-data-screening` | S1 data shape |

## Regression Checks

- Never use deprecated `pairwise_ttests`.
- Never use `tail=`; use `alternative=`.
- For Pingouin 0.6.1, use `pg.logistic_regression(X, y, ...)`.
- `$pingouin-stat` is the preferred main entry; router is compatibility-only.
- Final conclusions should pass `pg-analysis-approval` or include required revision/blocking notes.
- Keep each `SKILL.md` below 3600 bytes unless there is a clear reason.
- Prefer gate codes over repeated long caveats.
