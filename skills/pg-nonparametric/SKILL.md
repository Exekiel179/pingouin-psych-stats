---
name: pg-nonparametric
description: Run or generate Pingouin code for rank-based non-parametric tests — Mann-Whitney U, Wilcoxon signed-rank, Kruskal-Wallis, Friedman, and Cochran Q — when outcomes are ordinal or parametric assumptions fail.
---

# PG Nonparametric

Use when the outcome is ordinal, or continuous but non-normal with small n, so a rank-based test is safer than a t test or ANOVA.

## Load

Read:

- `../../references/supervision-gates.md`
- `../../references/pingouin-api-quickref.md`
- `../../references/apa-output-template.md` if writing results.

## Decision Rules

- Two independent groups -> `pg.mwu(x, y)` (Mann-Whitney U).
- Same participants measured twice / paired -> `pg.wilcoxon(x, y)` (signed-rank).
- Three or more independent groups, one factor -> `pg.kruskal(data, dv, between)`.
- Three or more repeated conditions, continuous/ordinal -> `pg.friedman(data, dv, within, subject)`.
- Three or more repeated conditions, binary outcome -> `pg.cochran(data, dv, within, subject)`.
- Follow a significant omnibus with `pg.pairwise_tests(..., parametric=False, padjust="holm")`.

## Required Inputs

- Outcome column and its scale (ordinal or non-normal continuous).
- Grouping (between) or condition (within) column.
- Subject ID for paired/repeated designs.
- Post hoc correction: default `holm`.
- Alternative hypothesis: default `two-sided` (mwu/wilcoxon only).

## Code Patterns

Mann-Whitney U (independent):

```python
x = df.loc[df["group"].eq("A"), "score"]
y = df.loc[df["group"].eq("B"), "score"]
res = pg.mwu(x, y, alternative="two-sided").round(3)
pg.print_table(res)
```

Wilcoxon signed-rank (paired):

```python
res = pg.wilcoxon(df["pre"], df["post"], alternative="two-sided").round(3)
pg.print_table(res)
```

Kruskal-Wallis (k independent groups):

```python
res = pg.kruskal(data=df, dv="score", between="group").round(3)
pg.print_table(res)
```

Friedman (k repeated conditions):

```python
res = pg.friedman(data=df, dv="score", within="condition", subject="id").round(3)
pg.print_table(res)
```

Cochran Q (binary repeated):

```python
res = pg.cochran(data=df, dv="passed", within="condition", subject="id").round(3)
pg.print_table(res)
```

## Output Checks

`mwu`/`wilcoxon` return `U_val`/`W_val`, `p_val`, `RBC` (rank-biserial), `CLES`. `kruskal` returns `H`, `ddof1`, `p_unc`; `friedman` returns Kendall `W`, `Q`, `p_unc`; `cochran` returns `Q`, `dof`, `p_unc`. Report the effect size, not just p.

## Guardrails

- `mwu` is unpaired only; `wilcoxon` is paired only — do not swap them.
- Kruskal/Friedman/Cochran are omnibus; always follow a significant result with corrected pairwise tests.
- Rank tests compare distributions/ranks, not means; word conclusions accordingly.
- Prefer parametric tests when their assumptions hold (more power).
- End result-bearing answers with one compact S0-S5 audit line.
