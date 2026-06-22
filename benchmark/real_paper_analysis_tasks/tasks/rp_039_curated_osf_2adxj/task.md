# rp_039_curated_osf_2adxj: Nature Human Behaviour Repro - Newson et al. (2025)

## Source

- Journal: Nature Human Behaviour
- Paper URL/DOI: not recorded
- Repository: https://osf.io/2adxj/
- Repository platform: OSF
- Source language: English
- Verification status: `verified`
- Task status: `ready_for_source_linked_run`

## Research Context

- Research question: Extract exact research question from the Nature Human Behaviour article and robustness report.
- Article hypotheses: Extract focal predictions and robustness claims from the article/script.
- Experimental design: Inspect paper and repository for sample, measures, and correlational or experimental structure.
- Analysis type: correlation / robustness analysis
- Variables needed: Correlation variables and correction family from the script.
- Planned Pingouin route: `pg-correlations`

## Repository Evidence

- Data evidence: Correlation_BonfCorrected.xlsx
- Script evidence: R_codes_v3_Newsonetal.2025.qmd; Syntax-Reproducibility-Robustness.sps

## Benchmark Task

Starting from the research question, reconstruct the study design, identify the target hypothesis and variables, then produce a defensible analysis plan and result interpretation. Use the repository data/scripts when available. If file-level evidence is incomplete, explicitly state what must be verified before numeric reproduction.

## Expected Deliverables

- Research question reconstructed from the paper context.
- Article hypotheses or a clear statement that the hypothesis must be extracted from the paper.
- Experimental design summary: sample, factors, within/between-subject structure, measures, exclusions.
- Variable mapping from repository data/scripts to outcome, predictors, covariates, and participant IDs.
- Statistical method choice with assumptions and a note on whether Pingouin is in scope.
- Executable Python/Pingouin analysis code or a precise reason why the original method is outside Pingouin scope.
- APA-style or Chinese psychology-style result report.
- Interpretation tied back to the research question, with caveats and no unsupported causal claims.

## Known Failure Modes

- Analyzing a convenient variable instead of the paper's focal dependent variable.
- Ignoring repeated-measures, participant IDs, item IDs, or nested trial structure.
- Using an independent-samples test for paired/repeated observations.
- Omitting assumption checks, effect sizes, confidence intervals, or multiple-comparison correction.
- Reporting numeric results that were not computed from the referenced data/script.
- Interpreting a significant p value without linking it to the hypothesis.
- Making causal claims from correlational or cross-sectional data.
