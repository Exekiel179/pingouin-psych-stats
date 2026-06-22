# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

- `tasks/strict_007_rp_010_rr_010/sources/doc/VOORSPOELS_replication_raceerased_r.pdf` (doc, 174879 bytes)
- `tasks/strict_007_rp_010_rr_010/sources/other/OSF_README.rtf` (other, 55144 bytes)
- `tasks/strict_007_rp_010_rr_010/sources/doc/DETAILED_REPLICATION_PROPOSAL.pdf` (doc, 186368 bytes)
- `tasks/strict_007_rp_010_rr_010/sources/script/power_race_erased.R` (script, 2092 bytes)
- `tasks/strict_007_rp_010_rr_010/sources/doc/DETAILED_REPLICATION_PROPOSAL_update_after_testruns.pdf` (doc, 186368 bytes)
- `tasks/strict_007_rp_010_rr_010/sources/data/race_erased_replication2014.txt` (data, 251438 bytes)
- `tasks/strict_007_rp_010_rr_010/sources/data/race_erased_replication2014.xls` (data, 3822592 bytes)
- `tasks/strict_007_rp_010_rr_010/sources/script/data_preprocessing.R` (script, 5985 bytes)
- `tasks/strict_007_rp_010_rr_010/sources/script/data_analyses.R` (script, 10239 bytes)
- `tasks/strict_007_rp_010_rr_010/sources/other/race_erased.Rdata` (other, 14998 bytes)

## Script-Derived Analysis Clues

- Detected analysis families: t_test
- Candidate variables: coal_enc, condition, race_enc

Snippets:

- `pwr.t.test(n= , d=H1.dzp, sig.level=.05, power=.95 ,type=c("two.sample"), alternative=c("greater"))`
- `pwr.t.test(n= , d=H2.dzp, sig.level=.05, power=.95 ,type=c("two.sample"), alternative=c("greater"))`
- `H1 <- t.test(NOCUE_d$race_enc,CUE_d$race_enc,var.equal=TRUE, alternative="greater")`
- `H2 <- t.test(NOCUE_d$coal_enc,CUE_d$coal_enc,var.equal=FALSE, alternative="less")`
- `nc_race <- t.test(NOCUE_d$race_WC,NOCUE_d$race_BC,alternative="greater",paired=TRUE)`
- `nc_coalition <- t.test(NOCUE_d$coalition_WC,NOCUE_d$coalition_BC,alternative="greater",paired=TRUE)`
- `c_race <- t.test(CUE_d$race_WC,CUE_d$race_BC,alternative="greater",paired=TRUE)`
- `c_coalition <- t.test(CUE_d$coalition_WC,CUE_d$coalition_BC,alternative="greater",paired=TRUE)`

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
