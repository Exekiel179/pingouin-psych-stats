Use the local Pingouin plugin guidance at:
F:/plugins/pingouin-psych-stats/skills/pingouin-stat/SKILL.md
F:/plugins/pingouin-psych-stats/skills/pg-analysis-approval/SKILL.md
F:/plugins/pingouin-psych-stats/references/workflow-index.md
F:/plugins/pingouin-psych-stats/references/supervision-gates.md
F:/plugins/pingouin-psych-stats/references/pingouin-api-quickref.md

Apply the $pingouin-stat workflow: intake if needed, route, analyze, run approval, and report. Keep the response concise.

You are analyzing a statistical/data-analysis task.

Dataset path: tasks/data/statllm/DS0055/sample2014.xlsx

Data description:
This dataset named sample2014.xlxs contains survey results from 435 students enrolled at a university in the United States. The survey was
conducted during the Spring 2014 semester.

Variable Name Description                                           Type (In Data File) Measure (Actual) Value labels
ids           ID number                                                Numeric             Nominal
bday          Date of birth (mm/dd/yyyy) Date,                          mm/dd/yyyy          Scale
enrolldate    Date of college enrollment (mm/dd/yyyy)                   String              Scale
expgradate    Expected date of college graduation (mm/dd/yyyy)          String              Scale
Rank          Class rank                                                Numeric             Ordinal 1=Freshman 2=Sophomore 3=Junior 4=Senior
Major         Major                                                     String              Nominal
Gender        Gender                                                    Numeric             Nominal 0=Male 1=Female
Athlete       Is student an athlete?                                    Numeric             Nominal 0 = Non-athlete   1 = Athlete
Height        Height (inches)                                           Numeric             Scale
Weight        Weight (pounds)                                           Numeric             Scale
Smoking       Does student smoke?                                       Numeric             Nominal 0 = Nonsmoker 1 = Past smoker 2 = Current smoker
Sprint        35-meter sprint time (seconds)                            Numeric             Scale
MileMinDur    Mile run time (hh:mm:ss)                                  Datetime            Scale
English       Score on English placement test (out of 100 points)       Numeric             Scale
Reading       Score on Reading placement test (out of 100 points)       Numeric             Scale
Math          Score on Math placement test (out of 100 points)          Numeric             Scale
Writing       Score on Writing placement test (out of 100 points)       Numeric             Scale
State         Is student in-state or out-of-state resident?             String              Nominal
LiveOnCampus  Does student live on campus?                              Numeric             Nominal 0 = Off-campus 1 = On-campus
HowCommute    How does student commute to campus?                       Numeric             Nominal 1 = Walk 2 = Bike 3 = Car 4 = Public transit 5 = Other
CommuteTime   How long does it take you to commute to campus?(minutes)  Numeric             Scale
SleepTime     About how many hours of sleep do you get per night?       Numeric             Scale
StudyTime     About how many hours per week do you study?               Numeric             Scale

Reference: https://libguides.library.kent.edu/SAS/

Task:
For the dataset sample2014, use a bivariate Pearson Correlation to test whether there is a statistically significant linear relationship between height and weight,
and to determine the strength and direction of the association.

Return:
1. Brief method choice.
2. Executable Python code.
3. Final answer in the requested format if any.
4. Any assumptions or limitations.

