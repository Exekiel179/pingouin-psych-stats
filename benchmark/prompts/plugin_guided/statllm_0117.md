Use the local Pingouin plugin guidance at:
F:/plugins/pingouin-psych-stats/skills/pingouin-stat/SKILL.md
F:/plugins/pingouin-psych-stats/skills/pg-analysis-approval/SKILL.md
F:/plugins/pingouin-psych-stats/references/workflow-index.md
F:/plugins/pingouin-psych-stats/references/supervision-gates.md
F:/plugins/pingouin-psych-stats/references/pingouin-api-quickref.md

Apply the $pingouin-stat workflow: intake if needed, route, analyze, run approval, and report. Keep the response concise.

You are analyzing a statistical/data-analysis task.

Dataset path: tasks/data/statllm/DS0030/hsb2.csv

Data description:
1, Name: hsb2

2. Data Set Information: 
This data file contains 200 observations from a sample of high school students with demographic information about the students, such as their gender (female), socio-economic status (ses) and ethnic background (race). It also contains a number of scores on standardized tests, including tests of reading (read), writing (write), mathematics (math) and social studies(socst). 

3. Attribute Information:

Number of Obs: 200
Number of Variables: 11

Attribute: Attribute Range

(1). Id:  student id number from 1 to 200
(2). Female: 0 for male and 1 for female
(3). Race: ethnic background, four kinds of races
(4). Scocst: social studies
(5). schtyp: normal bimodal
(6). Math: mathematics 
(7). Write: writing
(8). Read: reading
(9). Socst: socio-economic status;
(10). Prog
(11). Science
 





Reference:

The raw data comes from https://stats.oarc.ucla.edu/sas/whatstat/what-statistical-analysis-should-i-usestatistical-analyses-using-sas/

Citation: required

Task:
For the dataset of hsb2, test whether the mean of write differs between the three program types (prog).

Return:
1. Brief method choice.
2. Executable Python code.
3. Final answer in the requested format if any.
4. Any assumptions or limitations.

