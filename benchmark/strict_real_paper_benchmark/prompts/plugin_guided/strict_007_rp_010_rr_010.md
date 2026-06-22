Use `$pingouin-stat` and `$pg-analysis-approval`.
Route to the smallest applicable Pingouin workflow. If the original script uses a method outside Pingouin scope, state that explicitly and give the closest safe Pingouin subset only if defensible.

You are completing a strict real-paper psychology benchmark task.

Paper: Voorspoels 2014 registered report
Journal: Frontiers in Psychology
Paper URL/DOI: https://doi.org/10.3389/fpsyg.2014.01035
Original repository: https://osf.io/vnhrm/

Local data files:
- tasks/strict_007_rp_010_rr_010/sources/data/race_erased_replication2014.txt
- tasks/strict_007_rp_010_rr_010/sources/data/race_erased_replication2014.xls

Local script files:
- tasks/strict_007_rp_010_rr_010/sources/script/power_race_erased.R
- tasks/strict_007_rp_010_rr_010/sources/script/data_preprocessing.R
- tasks/strict_007_rp_010_rr_010/sources/script/data_analyses.R

Local document/readme files:
- tasks/strict_007_rp_010_rr_010/sources/doc/VOORSPOELS_replication_raceerased_r.pdf
- tasks/strict_007_rp_010_rr_010/sources/doc/DETAILED_REPLICATION_PROPOSAL.pdf
- tasks/strict_007_rp_010_rr_010/sources/doc/DETAILED_REPLICATION_PROPOSAL_update_after_testruns.pdf

Detected analysis families from scripts: t_test
Candidate variables from scripts: coal_enc, condition, race_enc
Script analysis snippets:
- `pwr.t.test(n= , d=H1.dzp, sig.level=.05, power=.95 ,type=c("two.sample"), alternative=c("greater"))`
- `pwr.t.test(n= , d=H2.dzp, sig.level=.05, power=.95 ,type=c("two.sample"), alternative=c("greater"))`
- `H1 <- t.test(NOCUE_d$race_enc,CUE_d$race_enc,var.equal=TRUE, alternative="greater")`
- `H2 <- t.test(NOCUE_d$coal_enc,CUE_d$coal_enc,var.equal=FALSE, alternative="less")`
- `nc_race <- t.test(NOCUE_d$race_WC,NOCUE_d$race_BC,alternative="greater",paired=TRUE)`
- `nc_coalition <- t.test(NOCUE_d$coalition_WC,NOCUE_d$coalition_BC,alternative="greater",paired=TRUE)`
- `c_race <- t.test(CUE_d$race_WC,CUE_d$race_BC,alternative="greater",paired=TRUE)`
- `c_coalition <- t.test(CUE_d$coalition_WC,CUE_d$coalition_BC,alternative="greater",paired=TRUE)`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
