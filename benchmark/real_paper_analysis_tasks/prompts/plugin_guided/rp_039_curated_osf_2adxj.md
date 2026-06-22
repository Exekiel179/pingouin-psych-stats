Use `$pingouin-stat` for this task. Follow its workflow:
1. clarify only if necessary,
2. route to the smallest Pingouin workflow,
3. analyze with Pingouin where in scope,
4. run `$pg-analysis-approval` checks before interpretation,
5. report concisely.

Expected route hint: `pg-correlations`.

You are completing a real-paper psychology analysis benchmark task.

Paper: Nature Human Behaviour Repro - Newson et al. (2025)
Journal: Nature Human Behaviour
Paper URL/DOI: not recorded
Repository: https://osf.io/2adxj/
Repository platform: OSF
Source language: English
Verification status: verified

Research question:
Extract exact research question from the Nature Human Behaviour article and robustness report.

Article hypotheses:
Extract focal predictions and robustness claims from the article/script.

Experimental design:
Inspect paper and repository for sample, measures, and correlational or experimental structure.

Data/script evidence:
- Data: Correlation_BonfCorrected.xlsx
- Script: R_codes_v3_Newsonetal.2025.qmd; Syntax-Reproducibility-Robustness.sps

Requested task:
Starting from the research question, reconstruct the experimental design, identify the hypothesis and variables, route to the appropriate analysis, provide Python/Pingouin code when in scope, and interpret the result in relation to the paper's claim. If data/scripts are not fully accessible, provide a precise verification gap and a reproducible analysis plan instead of inventing numbers.

Expected deliverables:
- Research question reconstructed from the paper context.
- Article hypotheses or a clear statement that the hypothesis must be extracted from the paper.
- Experimental design summary: sample, factors, within/between-subject structure, measures, exclusions.
- Variable mapping from repository data/scripts to outcome, predictors, covariates, and participant IDs.
- Statistical method choice with assumptions and a note on whether Pingouin is in scope.
- Executable Python/Pingouin analysis code or a precise reason why the original method is outside Pingouin scope.
- APA-style or Chinese psychology-style result report.
- Interpretation tied back to the research question, with caveats and no unsupported causal claims.

Known failure modes to avoid:
- Analyzing a convenient variable instead of the paper's focal dependent variable.
- Ignoring repeated-measures, participant IDs, item IDs, or nested trial structure.
- Using an independent-samples test for paired/repeated observations.
- Omitting assumption checks, effect sizes, confidence intervals, or multiple-comparison correction.
- Reporting numeric results that were not computed from the referenced data/script.
- Interpreting a significant p value without linking it to the hypothesis.
- Making causal claims from correlational or cross-sectional data.

Return format:
1. Source verification.
2. Research question and hypotheses.
3. Experimental design and variable map.
4. Analysis route and assumptions.
5. Python/Pingouin code or justified out-of-scope note.
6. Result reporting template or reproduced result if available.
7. Interpretation and limitations.

