# Benchmark Task Inventory

Total tasks: 49

## Counts
- StatLLM: 37
- InfiAgent DA-Agent/DAEval: 12
- screening: 18
- correlation: 16
- anova: 9
- descriptive: 7
- regression: 6
- mean_tests: 5
- chi_square: 1
- other: 1

## Tasks

| ID | Source | Tags | Dataset | Prompt |
| --- | --- | --- | --- | --- |
| `statllm_0003` | StatLLM | anova | `tasks/data/statllm/DS0002/copper.csv` | For the copper dataset, conduct an ANOVA analysis for the respone variable warp with respect to factors temperature and pecentage with interaction. |
| `statllm_0004` | StatLLM | anova | `tasks/data/statllm/DS0002/copper.csv` | For the copper dataset, conduct an two-way ANOVA analysis for the respone variable warp with respect to factors temperature and pecentage with interaction. |
| `statllm_0005` | StatLLM | anova | `tasks/data/statllm/DS0002/copper.csv` | For the copper dataset, conduct an one-way ANOVA analysis for the respone variable warp with respect to the factor temperature. |
| `statllm_0007` | StatLLM | regression | `tasks/data/statllm/DS0003/crack.csv` | For the crack dataset, do a simple linear regression and plot the result from PROC REG. The response is load and the covariate is age. |
| `statllm_0013` | StatLLM | anova | `tasks/data/statllm/DS0004/toxic.csv` | For the toxic dataset, conduct an two-way ANOVA analysis for the respone variable life with respect to factors poison and treatment with interaction. |
| `statllm_0017` | StatLLM | descriptive | `tasks/data/statllm/DS0005/sleeptime.csv` | For the sleep dataset, what is a 90% confidence interval for the population average sleeping time, based on the sample? Is there evidence that the true population mean hours of ... |
| `statllm_0021` | StatLLM | screening | `tasks/data/statllm/DS0008/soil.csv` | For the soil dataset, the question is to test whether the gap and growth areas do not differ with respect to soil respiration. According to the Normality check of the data, the ... |
| `statllm_0022` | StatLLM | screening | `tasks/data/statllm/DS0009/horse.csv` | For the horse dataset, the question is to test whether the densities of two sites are different. The data of two sites (of the same horse) are dependent, futher analysis also sh... |
| `statllm_0025` | StatLLM | anova | `tasks/data/statllm/DS0011/retention.csv` | For the retention dataset, conduct a two-way ANOVA analysis with interaction. |
| `statllm_0027` | StatLLM | screening | `tasks/data/statllm/DS0012/poplar.csv` | For the poplar dataset, the research question is to test whether the poplar tree weights are different under the four treatments. The weight samples are not normally distributed. |
| `statllm_0036` | StatLLM | regression, screening | `tasks/data/statllm/DS0019/measurement.csv` | For the measurement dataset, after fiting the regression model of height on weight. We want to check regression assumptions such as the linear relationship between two variables... |
| `statllm_0040` | StatLLM | screening | `tasks/data/statllm/DS0006/read.csv` | For the read dataset, create QQplots and test statistics for accessing Normality for the grade variable for each method. |
| `statllm_0061` | StatLLM | anova, screening | `tasks/data/statllm/DS0024/imports.csv` | For the imports dataset, fit anova model with horsepower (hp) versus fueltypes, aspiration and drivewheels. |
| `statllm_0062` | StatLLM | screening | `tasks/data/statllm/DS0026/glassid.csv` | For the dataset of glassid, test normality of Na for glass type (grouped type) of headlamps (glass type). |
| `statllm_0065` | StatLLM | descriptive | `tasks/data/statllm/DS0026/glassid.csv` | For the glassid dataset, do a hypethesis test to check whether mean of RI of glass type of buildingwindow is significantly different from 1.52. |
| `statllm_0075` | StatLLM | correlation | `tasks/data/statllm/DS0026/glassid.csv` | For the dataset of glassid, obtain Pearson correlation matrix for the numeric variables for glass types of vehicle windows (groupedtype) and headlamps combined(groupedtype). |
| `statllm_0076` | StatLLM | correlation | `tasks/data/statllm/DS0026/glassid.csv` | For the dataset of glassid, construct Pearson correlation matrix of all numerical variables. |
| `statllm_0086` | StatLLM | regression | `tasks/data/statllm/DS0042/measurement.csv` | For the dataset of measurement, perform a regression analysis with weight versus height. |
| `statllm_0088` | StatLLM | correlation, anova, screening | `tasks/data/statllm/DS0027/abalone.csv` | For the dataset of abalone, assuming normality, perform a one-way ANOVA for whole_weight with sex as the categorical predictor. |
| `statllm_0089` | StatLLM | correlation, mean_tests, anova, screening | `tasks/data/statllm/DS0027/abalone.csv` | For the dataset of abalone, perform a one-way ANOVA for whole_weight with sex as the categorical predictor. Perform turkey's test, Homogeneity of Variance, Welch's t-test, pairw... |
| `statllm_0092` | StatLLM | chi_square, screening | `tasks/data/statllm/DS0044/auto.csv` | For the dataset of auto, request a chi-square test that tests if rep78 and foreign are independent. |
| `statllm_0093` | StatLLM | mean_tests, screening | `tasks/data/statllm/DS0044/auto.csv` | For the dataset of auto, perform a t-test to determine whether the average mpg for domestic cars differ from the foreign cars. |
| `statllm_0098` | StatLLM | regression, screening | `tasks/data/statllm/DS0024/imports.csv` | For the dataset of imports, consumers wonder whether heavier cars have bigger engines: obtain a linear regression model for engine size as a function of curb weight. |
| `statllm_0101` | StatLLM | correlation, anova | `tasks/data/statllm/DS0043/manova.csv` | For the dataset of manova, calculate the correlation matrix among useful, difficulty and importance. |
| `statllm_0105` | StatLLM | regression, screening | `tasks/data/statllm/DS0024/imports.csv` | For the dataset of imports, Based on the regression model with engine size versus curb weight, horsepower and city mpg, Comment on whether the model is significant and how much ... |
| `statllm_0115` | StatLLM | screening, descriptive | `tasks/data/statllm/DS0030/hsb2.csv` | For the dataset of hsb2, test whether the mean for write is the same for males and females. |
| `statllm_0117` | StatLLM | screening, descriptive | `tasks/data/statllm/DS0030/hsb2.csv` | For the dataset of hsb2, test whether the mean of write differs between the three program types (prog). |
| `statllm_0119` | StatLLM | regression | `tasks/data/statllm/DS0032/binary.csv` | For the dataset of binary, Perform logistic regression with outcome variable admit/don't admit versus GRE, GPA and rank. |
| `statllm_0120` | StatLLM | mean_tests | `tasks/data/statllm/DS0033/diabetic.csv` | For the dataset of diabetic, since each patient is observed twice, do the paired t-test for diabetic dataset. |
| `statllm_0123` | StatLLM | mean_tests | `tasks/data/statllm/DS0036/FERT.csv` | For the dataset of FERT, perform the two sample t-test for FRET data set to compare the effect of two brand fertilizer |
| `statllm_0155` | StatLLM | correlation | `tasks/data/statllm/DS0055/sample2014.xlsx` | For the dataset sample2014, use a bivariate Pearson Correlation to test whether there is a statistically significant linear relationship between height and weight, and to determ... |
| `statllm_0157` | StatLLM | descriptive | `tasks/data/statllm/DS0055/sample2014.xlsx` | Using dataset sample2014, do an Independent Samples t Test to compare the mean writing scores for males and females. |
| `statllm_0158` | StatLLM | mean_tests | `tasks/data/statllm/DS0055/sample2014.xlsx` | Using dataset sample2014, do a paired t test to test if there was a significant difference in the average of the two tests, English and Math. |
| `statllm_0177` | StatLLM | descriptive | `tasks/data/statllm/DS0059/mvreg.csv` | For the dataset of mvreg, calculate the mean and standard deviation of variable locus_of_control, self_concept, motivation, read, write, and science. |
| `statllm_0179` | StatLLM | correlation | `tasks/data/statllm/DS0059/mvreg.csv` | For the dataset of mvreg, calculate the pairwise correlation among locus_of_control, self_concept, and motivation. |
| `statllm_0183` | StatLLM | correlation | `tasks/data/statllm/DS0060/fitness.csv` | For the dataset of fitness, Obtain pairwise correlation table among variables Oxygen, RunTime, Age, Weight, RunPulse, MaxPulse, and RestPulse. |
| `statllm_0189` | StatLLM | descriptive | `tasks/data/statllm/DS0062/Test.csv` | For the dataset of test, generates N, Mean, Standard Deviation, Minimum and Maximum statistics of variables from q1 to q5. |
| `da_0005` | InfiAgent DA-Agent/DAEval | correlation | `tasks/data/da_agent/test_ave.csv` | Generate a new feature called "FamilySize" by summing the "SibSp" and "Parch" columns. Then, calculate the Pearson correlation coefficient (r) between the "FamilySize" and "Fare... |
| `da_0010` | InfiAgent DA-Agent/DAEval | screening | `tasks/data/da_agent/GODREJIND.csv` | Check if the "Total Traded Quantity" column adheres to a normal distribution. |
| `da_0011` | InfiAgent DA-Agent/DAEval | correlation | `tasks/data/da_agent/GODREJIND.csv` | Calculate the correlation coefficient between the "High Price" column and the "Low Price" column. |
| `da_0025` | InfiAgent DA-Agent/DAEval | screening | `tasks/data/da_agent/insurance.csv` | Check if the distribution of BMI values in the dataset follows a normal distribution. |
| `da_0026` | InfiAgent DA-Agent/DAEval | correlation | `tasks/data/da_agent/insurance.csv` | Calculate the correlation coefficient between the charges incurred by individuals and the number of children they have. |
| `da_0034` | InfiAgent DA-Agent/DAEval | correlation | `tasks/data/da_agent/imp.score.ldlr.metabolome.csv` | Is there a correlation between the "row retention time" and "importance.score" columns? |
| `da_0057` | InfiAgent DA-Agent/DAEval | correlation | `tasks/data/da_agent/estimated_numbers.csv` | Is there a correlation between the number of cases and the number of deaths recorded? |
| `da_0109` | InfiAgent DA-Agent/DAEval | other | `tasks/data/da_agent/test_Y3wMUE5_7gLdaTN.csv` | Explore the distribution of the LoanAmount column based on different values of the Education column. Determine if there is a significant difference in the loan amount between in... |
| `da_0730` | InfiAgent DA-Agent/DAEval | correlation | `tasks/data/da_agent/gapminder_cleaned.csv` | Is there a correlation between population and GDP per capita for the recorded years and countries in the dataset? |
| `da_0734` | InfiAgent DA-Agent/DAEval | correlation | `tasks/data/da_agent/gapminder_cleaned.csv` | Is there a correlation between life expectancy and GDP per capita for each continent? Perform correlation analysis for each continent separately and provide the correlation coef... |
| `da_0738` | InfiAgent DA-Agent/DAEval | screening | `tasks/data/da_agent/Credit.csv` | Check if the distribution of the "Age" column in the Credit.csv file adheres to a normal distribution. |
| `da_0739` | InfiAgent DA-Agent/DAEval | correlation | `tasks/data/da_agent/Credit.csv` | Determine the correlation coefficient between the "Limit" and "Balance" columns in the Credit.csv file. |
