# Pingouin-Specific Optimization Rules

Load this reference when generating or reviewing concrete Pingouin code.

## API and Version Safety

- Record `pingouin.__version__` in the run manifest.
- Inspect `inspect.signature(pg.function)` when a signature is uncertain; prefer the installed version over memory.
- Prefer `pairwise_tests`; do not use deprecated `pairwise_ttests`.
- Keep `alternative="two-sided"` unless a directional hypothesis was specified in advance.

## Design-Specific Defaults

- Use long format plus a stable subject ID for `rm_anova`, `mixed_anova`, `pairwise_tests` with `within`, `rm_corr`, `friedman`, and `cochran`.
- Check `pg.sphericity` and report the corrected p-value when repeated-measures sphericity is relevant.
- For unequal variances in one-way independent designs, consider `pg.welch_anova` and `pg.pairwise_gameshowell`.
- For multi-comparison families, set `padjust` explicitly (default `holm` unless a preregistered plan says otherwise).
- For regression and mediation, make missing-data handling explicit; for mediation, record `n_boot` and `seed`.
- For reliability, report the exact ICC model (`ICC1`, `ICC2`, etc.), not only the largest coefficient.
- For Bayes factors, report the prior scale and distinguish `BF10` from `BF01`.

## Output Contract

Before prose, inspect `res.columns` and preserve the raw result table. Prefer effect sizes, confidence intervals, correction labels, and sample sizes over p-values alone. Round only in the presentation layer, not before saving raw output.

## Refusal Boundaries

Do not force Pingouin onto mixed-effects/random-slope models, SEM, multilevel mediation, count models, survival analysis, or complex survey weights. Route those designs to an appropriate external package and record the reason in `audit.md`.
