# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_013_rp_022_rr_022/sources/data/Pilot_Anonymized_Data.csv` (data, 7081 bytes)
- `tasks/strict_013_rp_022_rr_022/sources/doc/Pilot_Results.pdf` (doc, 715631 bytes)
- `tasks/strict_013_rp_022_rr_022/sources/script/Pilot_Syntax_Code.r` (script, 6620 bytes)
- `tasks/strict_013_rp_022_rr_022/sources/doc/Pilot_Codebook.pdf` (doc, 473646 bytes)
- `tasks/strict_013_rp_022_rr_022/sources/data/codebook_OstracismIngroupOutgroup.xls` (data, 83456 bytes)
- `tasks/strict_013_rp_022_rr_022/sources/data/OstracismIngroupOutgroupRawDataAnonymized.xlsx` (data, 434347 bytes)
- `tasks/strict_013_rp_022_rr_022/sources/script/RcodeOstracismIngroupOutgroup.r` (script, 31528 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: anova, t_test, correlation, regression, reliability
- Candidate variables: density, drink, fatrate, groupstatusc, idtot, jantemp, style, wdiffattrib, wdiffattribmoy

Snippets:

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

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
