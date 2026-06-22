---
name: pg-power
description: Plan psychology study sample sizes or compute achieved power with Pingouin power functions for t tests, ANOVA, repeated-measures ANOVA, and correlations.
---

# PG Power

Use when the user asks for sample size, power, detectable effect, or planning assumptions.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md`

## Function Choice

- One-sample, paired, or equal-n two-sample t test -> `pg.power_ttest`.
- Unequal independent groups -> `pg.power_ttest2n`.
- Between-subject ANOVA -> `pg.power_anova`.
- Repeated-measures ANOVA -> `pg.power_rm_anova`.
- Correlation -> `pg.power_corr`.

## Required Inputs

- Target test and design.
- Effect size assumption and source: prior study, smallest effect size of interest, pilot, or convention.
- Alpha.
- Desired power, usually .80 or .90.
- Tail/alternative and allocation ratio where relevant.
- Number of groups or repeated measurements.

## Code Patterns

Two-sample t test:

```python
n = pg.power_ttest(d=0.5, n=None, power=0.80,
                   alpha=0.05, contrast="two-samples")
print(n)
```

Unequal groups:

```python
power = pg.power_ttest2n(nx=30, ny=45, d=0.5, alpha=0.05)
print(power)
```

Correlation:

```python
n = pg.power_corr(r=0.3, n=None, power=0.80, alpha=0.05)
print(n)
```

ANOVA:

```python
n = pg.power_anova(eta_squared=0.06, k=3, n=None,
                   power=0.80, alpha=0.05)
print(n)
```

## Reporting

State:

- Solved quantity.
- All fixed assumptions.
- Whether n is per group or total. If Pingouin output meaning is uncertain, verify with docs/help and say so.
- Attrition inflation if the user gives expected dropout.
- Sensitivity table for multiple plausible effect sizes when planning is uncertain.

## Guardrails

- Do not pretend conventional effect sizes are study-specific evidence.
- Do not compute post hoc power as if it adds evidential value beyond CI/effect size unless the user explicitly requests it.
- For complex mixed/nested designs, Pingouin power functions may be insufficient; recommend simulation or specialized tools.
- End planning answers with one compact S0-S5 audit line where relevant.
