import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly
import pandas as pd
from sklearn.impute import KNNImputer

### Assignment: Shark Attacks

## Question 1: What are the most dangerous types of sharks to humans?
## Question 2: Are children more likely to be attacked by sharks? 
## Question 3: Are shark attacks where sharks were provoked more or less dangerous?
## Question 4: Are certain activities more likely to result in a shark attack?

'''
If you feel you can't answer a question based on the dataset alone, feel free to find other datasets and use them in answering the questions.
For each answer you give not only answer the question but also write about the assumptions you made in answering the question. 
If an assumption or decision possibly created a bias please write about this as well.

'''

# Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table

# Reading in the dataset (global data on shark attacks)
path = "attacks.csv"
df = pd.read_csv(path, encoding='ISO-8859-1')   # "ISO-8859" needed to be able to read the downloaded file
print(df.head())


## Question 1: What are the most dangerous types of sharks to humans?
