Use the local Pingouin plugin guidance at:
F:/plugins/pingouin-psych-stats/skills/pingouin-stat/SKILL.md
F:/plugins/pingouin-psych-stats/skills/pg-analysis-approval/SKILL.md
F:/plugins/pingouin-psych-stats/references/workflow-index.md
F:/plugins/pingouin-psych-stats/references/supervision-gates.md
F:/plugins/pingouin-psych-stats/references/pingouin-api-quickref.md

Apply the $pingouin-stat workflow: intake if needed, route, analyze, run approval, and report. Keep the response concise.

You are analyzing a statistical/data-analysis task.

Dataset path: tasks/data/statllm/DS0004/toxic.csv

Data description:
The dataset name is toxic. 
The variable life is the response, which gives the life. 
The varialbe poison is a factor, which gives the poison type. 
The varialbe treatment is a factor, which gives the treatment type.

Task:
For the toxic dataset, conduct an two-way ANOVA analysis for the respone variable life with respect to factors poison and treatment with interaction.

Return:
1. Brief method choice.
2. Executable Python code.
3. Final answer in the requested format if any.
4. Any assumptions or limitations.

