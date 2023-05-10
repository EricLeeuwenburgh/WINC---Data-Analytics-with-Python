import pandas as pd
import numpy as np

### Question: Which 3 countries had the biggest change in temperatures looking at 10 year moving averages (10YMA) between 1961 and 2019?
### (For example: a country had a 10YMA of -3 in 1970 and a 10YMA of +8 in 2018 the change was 11)

''' 
Some tips:
- before starting this exercise: investigate separately how to calculate moving averages (use a search engine)
- you don't need to average out monthly temperature data, using the annual data is good enough
- you don't need to look at the standard deviation
- you may use groupby but you don't need to
- feel free to plot the temperature changes and the moving averages if that helps
'''

# Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table
# pd.options.display.max_columns = 75   # Allows to view more columns (default max = 20)

df = pd.read_csv("Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="ISO-8859-1")     # Temperature data from 1961 till 2019
#print(df.columns)   

## Filter out rows and columns (that aren't needed for this exercise)
df = df[(df["Months"] == "Meteorological year") & (df["Element Code"] == 7271)]       # Filter out monthly and standard deviation data

## Create a new column for each year of data and calculate the 10-year Moving Average for each new column
for year in range(1961, 2020):
    col_name = f"{year}_10Y_MA"
    try:
        df[col_name] = df.loc[:, f"Y{year-9}":f"Y{year}"].mean(skipna=False, axis=1)      # Axis=1 == column wise, skipna=False == if any value is a NaN then result is NaN
    except KeyError:
        df[col_name] = np.nan           # Stores NaN if MA can't be calculated (for the first 9 columns there isn't enough historical data)

## Setting new df to only view the 10Y_MA columns 
ma_columns = [f"{year}_10Y_MA" for year in range(1961, 2020)]
df = df.loc[:, ["Area"] + ma_columns]                                      
df_ma = df.loc[:, ma_columns]

## Drop the columns where values are NaN
df.dropna(axis=1, how="all", inplace=True)
df_ma.dropna(axis=1, how="all", inplace=True)

## Function to find the biggest delta for each row (country)
def max_diff(row):
    return row.max() - row.min()

## Creating a new column in the original df based on the df_ma data
df["max_delta_MA"] = df_ma.apply(max_diff, axis=1)

## Sorting and setting Area as index
sorted_df = df.sort_values(by="max_delta_MA", ascending=False)
sorted_df.set_index("Area", inplace=True)

#------------------------------------------------------------------------------------------------------------------------------------#

### Question: Which 3 countries had the biggest change in temperatures looking at the 10Y_MA between 1961 and 2019?
### Answer:
print("Top 3 - Countries with the biggest change in the 10Y_MA:")
print(sorted_df["max_delta_MA"].head(3))

'''
Note:
I'm using a for-loop to calculate the MA for all countries at a time.
It's probably better/easier to use the .rolling method (see solution: ".rolling(10).mean()")
The .rolling method hasn't been treated in the course though.
 
'''