---
name: pg-anova
description: Run or generate Pingouin code for one-way, factorial, repeated-measures, mixed, Welch ANOVA, ANCOVA, and follow-up pairwise tests.
---

# PG ANOVA

Use when the outcome is continuous and predictors are categorical factors, optionally with covariates or repeated measures.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md`
- `../../references/pingouin-optimization.md`
- `../../references/apa-output-template.md` if writing results.

## Function Choice

- One between-subject factor -> `pg.anova(data=df, dv=..., between=..., detailed=True)`.
- Multiple between-subject factors -> `pg.anova(data=df, dv=..., between=[...], detailed=True)`.
- Unequal variances in one-way between design -> consider `pg.welch_anova`.
- One or more within-subject factors -> `pg.rm_anova(..., within=..., subject=..., detailed=True)`.
- One within-subject factor plus one between-subject factor -> `pg.mixed_anova`.
- Between-subject factor plus continuous covariate -> `pg.ancova`.
- Follow-up contrasts -> `pg.pairwise_tests` with `padjust`.

## Required Inputs

- Dependent variable.
- Between-subject factor(s).
- Within-subject factor(s).
- Subject ID for repeated/mixed designs.
- Covariates for ANCOVA.
- Planned contrasts or post hoc intent.
- Desired effect size, if not Pingouin default.

## Code Patterns

One-way ANOVA:

```python
aov = pg.anova(data=df, dv="score", between="group", detailed=True).round(3)
pg.print_table(aov)
```

Repeated-measures ANOVA:

```python
aov = pg.rm_anova(data=df, dv="score", within="condition",
                  subject="id", detailed=True).round(3)
pg.print_table(aov)
```

Mixed ANOVA:

```python
aov = pg.mixed_anova(data=df, dv="score", within="time",
                     between="group", subject="id").round(3)
pg.print_table(aov)
```

Follow-up:

```python
posthoc = pg.pairwise_tests(data=df, dv="score", within="time",
                            between="group", subject="id",
                            padjust="holm", effsize="hedges").round(3)
pg.print_table(posthoc)
```

ANCOVA:

```python
aov = pg.ancova(data=df, dv="score", between="group", covar="baseline").round(3)
```

## Interpretation Checklist

- Identify omnibus effects before pairwise claims.
- For repeated-measures effects, check and report sphericity or corrected p-values if returned.
- Report effect size column present in output, commonly `np2`.
- Report correction used for post hoc comparisons.
- For interactions, do not interpret main effects as simple group differences unless appropriate.

## Guardrails

- `mixed_anova` is for a specific mixed design; do not use it for arbitrary multi-level nesting.
- Pingouin is not a full mixed-effects model package. For random slopes/nested clusters, recommend statsmodels/R lme4 instead.
- Do not run ANOVA on wide repeated-measures data until reshaped or a Pingouin function explicitly accepts that shape.
- If cell sizes are very small or missing cells exist, inspect design balance before trusting output.
- End result-bearing answers with one compact S0-S5 audit line.
