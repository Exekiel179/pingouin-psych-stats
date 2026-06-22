Use the local Pingouin plugin guidance at:
F:/plugins/pingouin-psych-stats/skills/pingouin-stat/SKILL.md
F:/plugins/pingouin-psych-stats/skills/pg-analysis-approval/SKILL.md
F:/plugins/pingouin-psych-stats/references/workflow-index.md
F:/plugins/pingouin-psych-stats/references/supervision-gates.md
F:/plugins/pingouin-psych-stats/references/pingouin-api-quickref.md

Apply the $pingouin-stat workflow: intake if needed, route, analyze, run approval, and report. Keep the response concise.

You are analyzing a statistical/data-analysis task.

Dataset path: tasks/data/statllm/DS0003/crack.csv

Data description:
The dataset name is crack. 
The variable id gives the id of the observation. 
The variable load is the response, which gives the load amount. 
The varialbe age is a covariate, which gives the age. 
The variable agef is a factor, which treats age as a factor.

Task:
For the crack dataset, do a simple linear regression and plot the result from PROC REG. The response is load and the covariate is age.

Return:
1. Brief method choice.
2. Executable Python code.
3. Final answer in the requested format if any.
4. Any assumptions or limitations.

