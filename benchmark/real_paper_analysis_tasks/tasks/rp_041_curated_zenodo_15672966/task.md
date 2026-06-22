# rp_041_curated_zenodo_15672966: Protracted development of gaze behavior

## Source

- Journal: Nature Human Behaviour
- Paper URL/DOI: https://doi.org/10.5281/zenodo.15672966
- Repository: https://zenodo.org/records/15672966
- Repository platform: Zenodo
- Source language: English
- Verification status: `needs_manual_check`
- Task status: `needs_file_verification`

## Research Context

- Research question: How does gaze behavior develop across age or developmental stage?
- Article hypotheses: Extract exact developmental predictions from the paper before final task release.
- Experimental design: Developmental eye-tracking dataset; inspect task, age groups, repeated trials, and participant IDs.
- Analysis type: developmental gaze-behavior analysis
- Variables needed: Age/development predictor, gaze outcome, participant/trial identifiers.
- Planned Pingouin route: `pg-anova`

## Repository Evidence

- Data evidence: Zenodo record title indicates raw eyetracking data for Nature Human Behaviour paper.
- Script evidence: Script/code evidence not confirmed in quick API search.

## Benchmark Task

Starting from the research question, reconstruct the study design, identify the target hypothesis and variables, then produce a defensible analysis plan and result interpretation. Use the repository data/scripts when available. If file-level evidence is incomplete, explicitly state what must be verified before numeric reproduction.

## Expected Deliverables

- Repository verification note: identify what data/script evidence is present and what remains missing.
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
