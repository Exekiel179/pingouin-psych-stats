# rp_038_curated_osf_wjr7u: Object-based encoding constrains storage in visual working memory

## Source

- Journal: Journal of Experimental Psychology: General
- Paper URL/DOI: not recorded
- Repository: https://osf.io/wjr7u/
- Repository platform: OSF
- Source language: English
- Verification status: `partial`
- Task status: `needs_result_freezing`

## Research Context

- Research question: How does object-based encoding constrain visual working-memory storage?
- Article hypotheses: Extract exact hypothesis statements from the published article before final task release.
- Experimental design: Visual working-memory experiment; inspect methods for condition structure and repeated-measures design.
- Analysis type: visual working-memory group/condition analysis
- Variables needed: Outcome accuracy/recall, condition/grouping variables, participant ID.
- Planned Pingouin route: `pg-anova`

## Repository Evidence

- Data evidence: OSF metadata: open data and code for accepted JEP:General paper.
- Script evidence: OSF metadata: open data and code for accepted JEP:General paper.

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
