You are completing a strict real-paper psychology benchmark task.

Paper: IJzerman 2014 registered report
Journal: Social Psychology
Paper URL/DOI: https://doi.org/10.1027/1864-9335/a000185
Original repository: https://osf.io/nrbjz/

Local data files:
- tasks/strict_012_rp_019_rr_019/sources/data/Meta_Shackelford.xlsx
- tasks/strict_012_rp_019_rr_019/sources/data/Study_3_for_Sharing.sav
- tasks/strict_012_rp_019_rr_019/sources/data/Meta_Shackelford.xlsx
- tasks/strict_012_rp_019_rr_019/sources/data/syntax_shackel.txt
- tasks/strict_012_rp_019_rr_019/sources/data/Study_1_for_sharing.sav
- tasks/strict_012_rp_019_rr_019/sources/data/Study_2_for_sharing.sav
- tasks/strict_012_rp_019_rr_019/sources/data/Meta_dataset_USANL.txt
- tasks/strict_012_rp_019_rr_019/sources/data/Study_4_MTurk_Study_for_Sharing.sav
- tasks/strict_012_rp_019_rr_019/sources/data/Meta_datasetshackel.txt

Local script files:
- tasks/strict_012_rp_019_rr_019/sources/script/Study_2_syntax.sps
- tasks/strict_012_rp_019_rr_019/sources/script/Study_4_MTurk_Syntax.sps
- tasks/strict_012_rp_019_rr_019/sources/script/Study_4_soi_sjs_mediation_just_heterosexual.sps
- tasks/strict_012_rp_019_rr_019/sources/script/Study_3_Syntax.sps
- tasks/strict_012_rp_019_rr_019/sources/script/Study_4_soi_sjs_mediation_just_bisexual_and_homosexual.sps

Local document/readme files:
- tasks/strict_012_rp_019_rr_019/sources/doc/Forest_v2.pdf

Detected analysis families from scripts: anova, correlation, regression, mediation, reliability
Candidate variables from scripts: not extracted
Script analysis snippets:
- `REGRESSION`
- `/STATISTICS COEFF OUTS R ANOVA`
- `*** Once including the standardized score of SOI, there is no longer an effect of gender. This suggests mediation.`
- `*** I therefore also checked a regression of gender onto SJS (basically replicating the t-test()`
- `/DESCRIPTIVES MEAN STDDEV CORR SIG N`
- `/STATISTICS COEFF OUTS R ANOVA CHANGE ZPP`
- `*** separately including SOI, without the interaction (in order to calculate full mediation). B = -.075, SE = .022.`
- `** http://www.danielsoper.com/statcalc3/calc.aspx?id=31) indicates that there is full mediation, Sobel's Z = 3.068, p = .002.`
- `*** Also tried it for age. We first standardized age again below to fit it into the regression.`
- `*** Now also including SOI. The age/gender interaction does not dissappear through SOI, so the effect obtained above is not a mediation through SOI. There is also no moderation of SOI. However, when excluding`
- `** gender from the analysis, the effect of age*soi appears. There may be a moderated mediation. Given that this is at an exploratory stage, the moderated mediation will be analyzed in a follow up study (for example, the`
- `** effect of the interaction term age*soi is at .112, and for a moderated mediation, the study is insufficiently powered).`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
