# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_011_rp_015_rr_015/sources/script/Murray_replication.Rmd` (script, 15980 bytes)
- `tasks/strict_011_rp_015_rr_015/sources/data/EDC_clean2.csv` (data, 170418 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: anova, t_test, correlation, regression, reliability
- Candidate variables: ManipCheck, P24NumNeg, cSelfEsteem, dCond, newdata2, rMood, rStateSE, rzPartnerEnh, zCloseness, zPercAccept

Snippets:

- `#Now fix up variable names to make it easier to calculate alpha/means later on`
- ````{r estimate alpha and create scale scores, include=FALSE}`
- `#Calculate alpha and also add mean score to data frame`
- `alpha(check.keys = TRUE) %$% keys,`
- `print(alphaObj$alpha)`
- `corr.test(newdata, y = NULL, use = "pairwise",method="pearson",adjust="holm",alpha=.05) #create correlation matrix with p values`
- `Cors <- cor(na.omit(newdata)) #create correlation matrix and save as "Cors"`
- `t.test(newdata2$ManipCheck~newdata2$Cond) #t test for difference in ManipCheck between conditions`
- `t.test(newdata2$P24NumNeg~newdata2$Cond) #t test for differences in guessed number of negative things partner listed`
- ````{r regression model testing interaction effect, echo=TRUE}`
- `#regression models`
- `m1 <- lm(ManipCheck~cSelfEsteem * dCond, data = newdata2) #DV = Manipulation Check`

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
