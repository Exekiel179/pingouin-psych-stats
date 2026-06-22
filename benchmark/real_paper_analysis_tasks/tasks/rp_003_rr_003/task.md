# rp_003_rr_003: Whillans 2017 registered report

## Source

- Journal: Comprehensive Results in Social Psychology
- Paper URL/DOI: https://doi.org/10.1080/23743603.2016.1273647
- Repository: https://osf.io/aqi5j/
- Repository platform: OSF
- Source language: English
- Verification status: `verified`
- Task status: `ready_for_source_linked_run`

## Research Context

- Research question: Extract from the article introduction/registered report rationale before final task release.
- Article hypotheses: Extract preregistered or stated hypotheses from the article before final task release.
- Experimental design: Extract participants, design factors, within/between-subject structure, measures, and exclusion rules from Methods.
- Analysis type: reproduce main inferential result
- Variables needed: Extract outcome, predictors/factors, covariates, and subject/repeated-measures identifiers from the original script/codebook.
- Planned Pingouin route: `pingouin-stat-router`

## Repository Evidence

- Data evidence: https://osf.io/aqi5j/
- Script evidence: https://osf.io/aqi5j/ (R, spss)

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
- Forcing the task into Pingouin when the original model may require mixed-effects or specialized software.
