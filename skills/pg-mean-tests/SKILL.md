---
name: pg-mean-tests
description: Run or generate Pingouin code for one-sample, independent, paired, Welch, and corrected pairwise mean comparisons in psychology studies.
---

# PG Mean Tests

Use for t tests and post hoc pairwise comparisons where the dependent variable is approximately continuous.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md`
- `../../references/apa-output-template.md` if writing results.

## Decision Rules

- One sample against a known value -> `pg.ttest(x, y=<value>)`.
- Two independent groups -> `pg.ttest(x, y, paired=False, correction="auto")`.
- Same participants measured twice -> `pg.ttest(x, y, paired=True)`.
- More than two group levels or multiple pairwise contrasts -> `pg.pairwise_tests`.
- Non-parametric pairwise comparisons -> `pg.pairwise_tests(..., parametric=False)`.

## Required Inputs

- Outcome column.
- Group or condition column.
- Subject ID for paired/repeated comparisons.
- Which comparisons are planned versus post hoc.
- Multiple-comparison correction: default to `holm` for post hoc families unless the user specifies another correction.
- Alternative hypothesis: default to `two-sided`.

## Code Patterns

Independent t test:

```python
x = df.loc[df["group"].eq("A"), "score"]
y = df.loc[df["group"].eq("B"), "score"]
res = pg.ttest(x, y, paired=False, correction="auto",
               alternative="two-sided", confidence=0.95).round(3)
pg.print_table(res)
```

Paired t test from wide columns:

```python
res = pg.ttest(df["pre"], df["post"], paired=True,
               alternative="two-sided", confidence=0.95).round(3)
pg.print_table(res)
```

Pairwise tests:

```python
res = pg.pairwise_tests(data=df, dv="score", between="group",
                        parametric=True, padjust="holm",
                        effsize="hedges").round(3)
pg.print_table(res)
```

Repeated pairwise tests:

```python
res = pg.pairwise_tests(data=df, dv="score", within="condition",
                        subject="id", padjust="holm",
                        effsize="hedges").round(3)
```

## Output Checks

Inspect `res.columns` before writing prose. Expected t-test columns often include `T`, `dof`, `p-val`, `CI95%`, `cohen-d`, `BF10`, and `power`.

## Guardrails

- Do not use deprecated `pairwise_ttests`.
- Do not call independent tests for paired data.
- Do not omit multiplicity correction for exploratory multi-comparison families.
- Report Welch/student choice when independent groups are imbalanced.
- If the outcome is ordinal or severely non-normal with small n, mention non-parametric alternatives.
- End result-bearing answers with one compact S0-S5 audit line.
