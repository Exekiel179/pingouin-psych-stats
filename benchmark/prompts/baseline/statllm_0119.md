You are analyzing a statistical/data-analysis task.

Dataset path: tasks/data/statllm/DS0032/binary.csv

Data description:
1, Name: binary

2. Data Set Information: 
This data set has a binary response (outcome, dependent) variable called admit, which is equal to 1 if the individual was admitted to graduate school, and 0 otherwise. There are three predictor variables: gre, gpa, and rank. We will treat the variables gre and gpa as continuous. The variable rank takes on the values 1 through 4. Institutions with a rank of 1 have the highest prestige, while those with a rank of 4 have the lowest.

3. Attribute Information:

Number of Obs: 400
Number of Variables: 4

Attribute: Attribute Range

(1). ADMIT 
(2). GRE
(3). GPA
(4). RANK

 



Reference:

https://stats.oarc.ucla.edu/sas/dae/logit-regression/

Citation: required

Task:
For the dataset of binary, Perform logistic regression with outcome variable admit/don't admit versus GRE, GPA and rank.

Return:
1. Brief method choice.
2. Executable Python code.
3. Final answer in the requested format if any.
4. Any assumptions or limitations.
