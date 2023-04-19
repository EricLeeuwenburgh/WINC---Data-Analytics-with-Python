import pandas as pd

# Exploring means taking a first look into the dataset and get a feeling for the data you are going the work with

cali_housing = pd.read_csv("sample_california_housing_test.csv")

print(cali_housing.head(5)) # show the first 5 rows
print(cali_housing.tail(8)) # show the last 8 rows

print(cali_housing.shape)   # this dataset has 3000 rows and 9 columns

print(cali_housing.size)    # give the total amount of values in the dataset

print(cali_housing.columns) # gives a array with all column names
print(cali_housing.dtypes)  # gives thr datatype per column

print(cali_housing.info())  # gives a small overview with general data about the dataset

print(cali_housing.describe())  # gives a statistical summary of the dataframe