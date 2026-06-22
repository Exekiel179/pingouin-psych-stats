Use `$pingouin-stat` and `$pg-analysis-approval`.
Route to the smallest applicable Pingouin workflow. If the original script uses a method outside Pingouin scope, state that explicitly and give the closest safe Pingouin subset only if defensible.

You are completing a strict real-paper psychology benchmark task.

Paper: Kvetnaya 2018 registered report
Journal: Journal of European Psychology Students
Paper URL/DOI: https://doi.org/10.5334/jeps.450
Original repository: https://osf.io/hba2p/

Local data files:
- tasks/strict_009_rp_012_rr_012/sources/data/subj01-20170515_1132.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj09-20170517_1327.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj21-20170523_1528.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj23-20170529_1125.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj04-20170516_1433.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj35-20170613_1440.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj03-20170516_1342.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj18-20170522_1204.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj30-20170612_1104.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj12-20170518_1530.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj02-20170515_1229.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj08-20170517_1235.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj24-20170529_1229.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj11-20170518_1425.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj39-20170616_1120.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj22-20170529_1024.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj14-20170519_1231.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj16-20170522_0837.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj38-20170616_1030.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj05-20170516_1531.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj26-20170531_1230.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj41-20170621_1258.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj13-20170518_1739.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj07-20170517_1144.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj10-20170518_1331.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj25-20170530_1424.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj33-20170612_1332.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj06-20170516_1631.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj32-20170612_1234.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj29-20170602_1541.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj37-20170613_1628.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj15-20170519_1344.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj20-20170523_1432.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj19-20170522_1250.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj27-20170531_1408.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj28-20170601_1329.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj17-20170522_0942.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj34-20170612_1526.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj31-20170612_1146.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj36-20170613_1533.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj40-20170616_1228.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj02-20170412_1440.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj03-20170421_1609.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj01-20170411_1154.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj03-20180517_1113.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj02-20180517_1030.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj01-20180517_0933.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj08-20180704_1102.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj39-20180719_1615.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj25-20180713_0853.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj09-20180704_1216.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj38-20180719_1158.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj27-20180713_1157.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj34-20180718_1013.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj07-20180704_0946.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj02-20180703_1058.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj03-20180703_1319.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj15-20180705_1111.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj20-20180710_1155.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj22-20180711_1458.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj33-20180717_1715.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj19-20180710_1007.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj23-20180712_1617.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj13-20180705_0911.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj29-20180713_1457.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj36-20180719_1002.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj28-20180713_1302.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj21-20180710_1500.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj30-20180713_1544.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj18-20180709_1157.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj31-20180717_1502.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj14-20180705_1001.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj01-20180703_0945.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj16-20180705_1201.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj37-20180719_1056.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj12-20180704_1754.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj26-20180713_1101.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj24-20180712_1716.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj11-20180704_1445.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj17-20180705_1245.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj32-20180717_1600.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj06-20180704_0900.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj40-20180719_1719.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj05-20180703_1555.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj04-20180703_1432.txt
- tasks/strict_009_rp_012_rr_012/sources/data/subj35-20180718_1306.txt

Local script files:
- tasks/strict_009_rp_012_rr_012/sources/script/spatialISEdata.R
- tasks/strict_009_rp_012_rr_012/sources/script/effectsizes.R
- tasks/strict_009_rp_012_rr_012/sources/script/power.R
- tasks/strict_009_rp_012_rr_012/sources/script/spatialISE_final.R
- tasks/strict_009_rp_012_rr_012/sources/script/verbalISE_pilot.R
- tasks/strict_009_rp_012_rr_012/sources/script/verbalISE.R
- tasks/strict_009_rp_012_rr_012/sources/script/power.R
- tasks/strict_009_rp_012_rr_012/sources/script/power_intact.R

Local document/readme files:
- tasks/strict_009_rp_012_rr_012/sources/doc/Registered_Replication_Report_Spatial_ISE_Final_Manuscript.pdf
- tasks/strict_009_rp_012_rr_012/sources/doc/Figure_1.pdf
- tasks/strict_009_rp_012_rr_012/sources/doc/Instructions_for_Participants_German.pdf
- tasks/strict_009_rp_012_rr_012/sources/doc/Registered_Replication_Report_Spatial_ISE.pdf
- tasks/strict_009_rp_012_rr_012/sources/doc/KvetnayaSchopf2019DAGA.pdf
- tasks/strict_009_rp_012_rr_012/sources/doc/Bachelor_Thesis_Verbal_ISE.pdf
- tasks/strict_009_rp_012_rr_012/sources/doc/Instructions_for_Participants_German.pdf
- tasks/strict_009_rp_012_rr_012/sources/doc/Figure_1.pdf

Detected analysis families from scripts: anova, t_test
Candidate variables from scripts: Error, as.numeric, err, err2, id, pos, snd, trial, tsk
Script analysis snippets:
- `# two-way repeated measures ANOVA`
- `m1 <- aov(err ~ snd*pos + Error(id/(snd*pos)), dat1)`
- `with(dat1, t.test(err[dat1$snd == "std"], err[dat1$snd == "chg"],`
- `m1 <- aov(y ~ snd*pos + Error(id/(snd*pos)), dat)`
- `m2 <- aov(y ~ snd*pos + Error(id/(snd*pos)), dat[dat$snd != "silence",])`
- `## For simulation: two-way setup; for ANOVA, collapse over position`
- `m1 <- aov(y ~ snd + Error(id/snd), aggregate(y ~ snd + id, dat, mean))`
- `dat.ttest <- aggregate(err ~ id + snd, dat1, sum)`
- `dat.ttest$err2 <- dat.ttest$err/7`
- `ttest <- with(dat.ttest, t.test(err2[dat.ttest$snd == "std"],`
- `err2[dat.ttest$snd == "chg"], paired = TRUE))`
- `m2 <- aov(err ~ snd*pos + Error(id/(snd*pos)), dat1[dat1$snd != "sil",])`

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
