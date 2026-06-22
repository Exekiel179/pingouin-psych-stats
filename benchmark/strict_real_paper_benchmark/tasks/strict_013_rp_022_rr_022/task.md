You are completing a strict real-paper psychology benchmark task.

Paper: Arpin 2017 registered report
Journal: Comprehensive Results in Social Psychology
Paper URL/DOI: https://doi.org/10.1080/23743603.2017.1358477
Original repository: https://osf.io/4mwn3/

Local data files:
- tasks/strict_013_rp_022_rr_022/sources/data/Pilot_Anonymized_Data.csv
- tasks/strict_013_rp_022_rr_022/sources/data/codebook_OstracismIngroupOutgroup.xls
- tasks/strict_013_rp_022_rr_022/sources/data/OstracismIngroupOutgroupRawDataAnonymized.xlsx

Local script files:
- tasks/strict_013_rp_022_rr_022/sources/script/Pilot_Syntax_Code.r
- tasks/strict_013_rp_022_rr_022/sources/script/RcodeOstracismIngroupOutgroup.r

Local document/readme files:
- tasks/strict_013_rp_022_rr_022/sources/doc/Pilot_Results.pdf
- tasks/strict_013_rp_022_rr_022/sources/doc/Pilot_Codebook.pdf

Detected analysis families from scripts: anova, t_test, correlation, regression, reliability
Candidate variables from scripts: density, drink, fatrate, groupstatusc, idtot, jantemp, style, wdiffattrib, wdiffattribmoy
Script analysis snippets:
- `# contains the variables implied in the regression model.`
- `# formula	the regression equation to be used`
- `fit <- lm(monModel,DF)`
- `alpha(data.frame(data.frame(DF$id1,DF$id2,DF$id3,DF$id4)))`
- `t.test(DF$idtot,mu=4) #  t = 2.32, p = .023`
- `fit<-lm(DF$idtot0~1,DF)`
- `cor.test(DF$attention_offender1,DF$attention_offender2)`
- `cor.test(DF$influence_offender1,DF$influence_offender2)`
- `cor.test(DF$inclusion_offender1,DF$inclusion_offender2)`
- `cor.test(DF$teamwork_offender1,DF$teamwork_offender2)  # r = .98`
- `cor.test(DF$angry_offender1,DF$angry_offender2) # r = .97`
- `cor.test(DF$sympathy_offender1,DF$sympathy_offender2) # r = .99`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
