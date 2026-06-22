Use the local Pingouin plugin guidance at:
F:/plugins/pingouin-psych-stats/skills/pingouin-stat/SKILL.md
F:/plugins/pingouin-psych-stats/skills/pg-analysis-approval/SKILL.md
F:/plugins/pingouin-psych-stats/references/workflow-index.md
F:/plugins/pingouin-psych-stats/references/supervision-gates.md
F:/plugins/pingouin-psych-stats/references/pingouin-api-quickref.md

Apply the $pingouin-stat workflow: intake if needed, route, analyze, run approval, and report. Keep the response concise.

You are analyzing a statistical/data-analysis task.

Dataset path: tasks/data/statllm/DS0044/auto.csv

Data description:
Data Description for SAS Dataset: AUTO

This dataset consists of automotive data including specifications and pricing for various car models. The dataset contains the following variables:

1. make (Character, Length = 20): The manufacturer and model of the car.
2. price (Numeric): The list price of the car in US dollars.
3. mpg (Numeric): Miles per gallon, indicating the fuel efficiency of the car.
4. rep78 (Numeric): Repair record from 1978, rated on a scale from 1 (poor) to 5 (excellent).
5. hdroom (Numeric): Headroom inside the car, measured in inches.
6. trunk (Numeric): Trunk space, measured in cubic feet.
7. weight (Numeric): Weight of the car, measured in pounds.
8. length (Numeric): Length of the car, measured in inches.
9. turn (Numeric): Turning circle of the car, measured in feet.
10. displ (Numeric): Engine displacement, measured in cubic centimeters.
11. gratio (Numeric): Gear ratio of the car.
12. foreign (Numeric): Binary indicator where 0 = Domestic car and 1 = Foreign car.

Data Input Method:
The data is input using the CARDS statement, which indicates that the data follows the INPUT statement line by line in the program file. Each line corresponds to a different car model with its respective specifications.

Example Data Entries:
- AMC Concord        4099  . 3 2.5 11 2930 186 40 121 3.58 0
- Audi 5000          9690 17 5 3.0 15 2830 189 37 131 3.20 1
- BMW 320i           9735 25 4 2.5 12 2650 177 34 121 3.64 1

Special Notes:
- Missing values are denoted by a period ('.') in this dataset.
- The variable 'make' is defined with a character length of 20, and input is taken from columns 1 to 17.
- Numeric data following the 'make' are input based on standard SAS numeric input rules.
- This dataset may be used for analysis of car specifications, price comparisons, and studying the differences between domestic and foreign car models.

Dataset Source:
This data is typically used for educational and analytical purposes in automotive studies, particularly in statistical analysis with SAS.

End of Data Description.

Reference:
https://stats.oarc.ucla.edu/sas/modules/an-overview-of-statistical-tests-in-sas/
Citation: required

Task:
For the dataset of auto, request a chi-square test that tests if rep78 and foreign are independent.

Return:
1. Brief method choice.
2. Executable Python code.
3. Final answer in the requested format if any.
4. Any assumptions or limitations.

