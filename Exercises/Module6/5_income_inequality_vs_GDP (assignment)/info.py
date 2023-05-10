import numpy as np
import pandas as pd
from scipy.stats import pearsonr

'''
Pearson correlation:

The Pearson correlation is a statistical measure that describes the strength and direction of the relationship 
between two continuous variables. It ranges from -1 to 1, where a value of 1 indicates a perfect positive relationship 
(as one variable increases, so does the other), a value of -1 indicates a perfect negative relationship 
(as one variable increases, the other decreases), and a value of 0 indicates no relationship between the two variables.

To calculate the Pearson correlation, you need to have two sets of data, and then you find the average of both sets, 
the standard deviation of each set, and then you multiply the deviations of both sets and sum them. Finally, you divide 
the sum by the product of the two standard deviations.

The Pearson correlation is often used in research to determine whether there is a relationship between two variables, 
such as the relationship between height and weight, or between age and income. It can help us understand how closely two 
variables are related and can be used to make predictions or draw conclusions based on the data.

Absolute Value      Interpretation
0.00 < 0.10         Negligible
0.10 < 0.20         Weak
0.20 < 0.40         Moderate
0.40 < 0.60         Relatively Strong
0.60 < 0.80         Strong
0.80 <= 1.00        Very Strong

----------------------------------------------------------------------------------------------------------------------------

P-value:
The p-value is a way to determine if the results of a study are meaningful or just happened by chance. It's like rolling 
a dice and getting a six, and then asking yourself: "Is this just luck or is the dice biased?". The p-value helps to answer 
that question by giving you a number that tells you how likely it is that the dice is biased. If the p-value is low, 
then it's unlikely that the result happened by chance, and you can conclude that the dice is probably biased. If the 
p-value is high, then it's likely that the result happened by chance, and you can't conclude that the dice is biased.

Similarly, in statistical analysis, if the p-value is low (usually less than 0.05), then it's unlikely that the observed 
results happened by chance alone, and you can conclude that there is a significant difference or relationship between the 
variables being studied. If the p-value is high (greater than 0.05), then it's likely that the observed results happened 
by chance, and you can't conclude that there is a significant difference or relationship between the variables.

Interpretation of P-value (standard)
Below 0.05 = Less likely to be based on chance alone (there is a relationship between the two variables)
Above 0.05 = More likely to be based on chance alone (there is no relationship between the two variables)

More on P-values: https://www.youtube.com/watch?v=kyjlxsLW1Is&list=PLICW5UpCwEj0duPGdUdkzkvbZ9zlhBbi_&index=1&t=567s

'''
# Generate data 
np.random.seed(1)  # for reproducibility

data = {
    'Start_Salary': np.random.randint(low=30000, high=50000, size=10),
    'Current_Salary': np.random.randint(low=50000, high=90000, size=10),
}

df = pd.DataFrame(data)
#print(df)

## Pandas correlation (doesn't show p-value)
print(df.corr())

## NumPy correlation (doesn't show p-value)
print(np.corrcoef(df["Start_Salary"], df["Current_Salary"]))

## SciPy correction (incl. p-value)
print(pearsonr(df["Start_Salary"], df["Current_Salary"]))