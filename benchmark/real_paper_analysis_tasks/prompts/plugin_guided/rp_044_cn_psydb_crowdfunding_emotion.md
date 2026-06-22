Use `$pingouin-stat` for this task. Follow its workflow:
1. clarify only if necessary,
2. route to the smallest Pingouin workflow,
3. analyze with Pingouin where in scope,
4. run `$pg-analysis-approval` checks before interpretation,
5. report concisely.

Expected route hint: `pg-anova`.

You are completing a real-paper psychology analysis benchmark task.

Paper: 公益众筹中如何提高项目吸引力：项目图片情绪效价和内容信息的作用
Journal: 心理学报
Paper URL/DOI: not recorded
Repository: https://www.scidb.cn/en/psych
Repository platform: ScienceDB/Psychological Science Data Bank
Source language: Chinese
Verification status: needs_manual_check

Research question:
项目图片情绪效价和内容信息如何影响公益众筹项目吸引力？

Article hypotheses:
提取关于情绪效价、内容信息及潜在交互/中介机制的假设。

Experimental design:
社会/消费心理实验；需核验图片情绪效价、内容信息操纵、吸引力评分和样本结构。

Data/script evidence:
- Data: ScienceDB/PsyDB search result indicates an Acta Psychologica Sinica related dataset.
- Script: Analysis script not confirmed; inspect dataset files.

Requested task:
Starting from the research question, reconstruct the experimental design, identify the hypothesis and variables, route to the appropriate analysis, provide Python/Pingouin code when in scope, and interpret the result in relation to the paper's claim. If data/scripts are not fully accessible, provide a precise verification gap and a reproducible analysis plan instead of inventing numbers.

Expected deliverables:
- Repository verification note: identify what data/script evidence is present and what remains missing.
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
- Misreading Chinese variable names, paper hypotheses, or psychology reporting conventions.

Return format:
1. Source verification.
2. Research question and hypotheses.
3. Experimental design and variable map.
4. Analysis route and assumptions.
5. Python/Pingouin code or justified out-of-scope note.
6. Result reporting template or reproduced result if available.
7. Interpretation and limitations.

