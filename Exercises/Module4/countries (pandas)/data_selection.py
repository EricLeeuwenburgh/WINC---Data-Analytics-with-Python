import pandas as pd

# most common used functions for selecting data:
# .loc[rows, columns]   to be used with strings
# .iloc[rows, columns]  only usable with integers, slices are not inclusive, faster  
# []index operator

smoking = pd.read_csv("sample_smoking_indicators.csv", sep=";", thousands=",")
print(smoking.head())

# Drop some columns for easier use
smoking.drop('la', inplace=True, axis=1)
smoking.drop(axis=1, columns=smoking.columns[5:], inplace=True)

# Rename columns
smoking.columns = ["boroughs", "current", "ex", "never", "total"]
print(smoking.head(5))

## Using .loc
# Select a single row
print(smoking.loc[0])

# Selecting multiple rows
print(smoking.loc[[0,10,21,0]])
print(smoking.loc[:2])      # .loc is inclusive. index[2] is included in the output

# Selecting a single column
print(smoking.loc[:,"current"])
print(smoking.loc[20:,['boroughs', 'ex']])

print(smoking.loc[20:,'boroughs': 'ex'])

# Selecting all column (default) explicitly
print(smoking.loc[20:,:])

# Use .set_index to set a specific column as the index column
smoking_name = smoking.set_index("boroughs")
print(smoking_name.head(5))
print(smoking_name.loc["Bexley":"Hackney", "ex":"never"])


## Using .iloc
# Select a single row
print(smoking.iloc[2])

# Selecting multiple rows and/or columns (not inclusive)
print(smoking.iloc[2:4])
print(smoking.iloc[2:4, 2:4])


## Passing in a callable (like a function)
def is_long_name(boroughs_name):
    return len(boroughs_name) > 12

mask = smoking.boroughs.apply(is_long_name) # == Boolean mask
print(smoking.loc[mask])

# Combining filters with the '|' or '&' operator
print(smoking.loc[(smoking.boroughs == "Bexley") | (smoking.boroughs == "Hackney")])
print(smoking.loc[(smoking.ex > 50000) & (smoking.current > 50000 )])

# Using the isin() function
print(smoking.loc[smoking.boroughs.isin(["Bexley", "Hackney", "Sutton"])])

# Using str.contains
print(smoking.loc[smoking.boroughs.str.contains("ham")])

# Using iloc, remember to use '.values' to make it a Numpy array
print(smoking.iloc[smoking.boroughs.str.contains("ham").values])