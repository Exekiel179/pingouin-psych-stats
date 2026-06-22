# rp_040_curated_osf_7wgv2: Robustness report: Arechar et al. (2023), Nature Human Behaviour

## Source

- Journal: Nature Human Behaviour
- Paper URL/DOI: not recorded
- Repository: https://osf.io/7wgv2/
- Repository platform: OSF
- Source language: English
- Verification status: `verified`
- Task status: `ready_for_source_linked_run`

## Research Context

- Research question: Extract exact research question from Arechar et al. and the robustness report.
- Article hypotheses: Extract focal hypothesis and robustness alternative specifications.
- Experimental design: Inspect paper and repository for participant structure, treatment/condition variables, and outcome.
- Analysis type: robustness / model comparison
- Variables needed: Outcome and model specification from Fig1 or supplement script.
- Planned Pingouin route: `pingouin-stat-router`

## Repository Evidence

- Data evidence: CR.csv; m_agg.rds; m_rob-alt.rds; m_rob-rev.rds
- Script evidence: Fig1-rev2.R; REP_supps-rev.Rmd; REP_supps.Rmd

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
