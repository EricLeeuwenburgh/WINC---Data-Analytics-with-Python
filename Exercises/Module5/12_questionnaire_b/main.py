import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

### Exercise: Scatterplot of latitude and longitude data

# Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table

# Reading in the dataset
df = pd.read_csv("qstn-b.csv")

# Removing the first column
df.drop(columns=["Unnamed: 0"], inplace=True)   # It's best to avoid using index values.

# Removing all "longitude" and "latitude" columns except for the first occurence (one each)
cols_to_drop = df.filter(like='lon').columns.tolist()[1:] + df.filter(like='lat').columns.tolist()[1:]  # removes columns: ['q7-lon', 'q8-lon']
df.drop(cols_to_drop, axis=1, inplace=True)
# Alternative (simple)
# df.drop(columns=["q7-lon", "q8-lat"])


## Cleaning data
# Finding (the amount of) null values and total values for each column

# Use Google Colab "datatables" to sort columns and look at .head() and .tail() values
# Creating a fast chart in Google Colab (% of missing values) = (df.isnull().median() * 100).plot(kind="bar")

df["resp. id"].info()               # Correct: according .info no null values present
df["datetime"].info()               ## Convertion: convert all values to type "datetime"
df["q1-bool"].unique()              ## Convertion: convert NaN to None
df["q2-lon"].describe()             ## Convertion: 0.0 values should be converted to NaN
df["q3-lat"].isnull().sum()         # Correct: apart from NaN no other null values found
df["q4-country"].isnull().sum()     ## Correction: convert NaN to None
df["q5-tld"].unique()               ## Convertion: "unknown" and "no domain" to be converted to None
df["q6-bool"].unique()              ## Convertion: convert NaN to None
df["q9-number"].isnull().sum()      # Correct: no weird values found, values + NaN = total == 20000

# Converting null values to default values (NaN, Nat or None)
df["datetime"].apply(pd.to_datetime)
df["q1-bool"].replace(np.nan, None, inplace=True) 
df["q2-lon"].replace(0, np.nan, inplace=True)
df["q4-country"].replace(np.nan, None, inplace=True)
df["q5-tld"].replace(["unknown", "no domain"], None, inplace=True)
df["q6-bool"].replace(np.nan, None, inplace=True)

# Removing (complete) rows which have a null value in the "lat" or "lon" columns
df.dropna(subset=["q2-lon", "q3-lat"], inplace=True)

# Create a new column with the number of missing values in that row
df["missing_value_count"] = df.isnull().sum(axis=1)

# Filter out the rows that have "0" missing values
df = df.loc[df['missing_value_count'] > 0]


## Scatterplot chart
plt.style.use("fivethirtyeight")
plt.figure(figsize=(10, 5))

latitude = df["q2-lon"]
longitude = df["q3-lat"]

plt.scatter(longitude, latitude, edgecolor='black', linewidth=1, alpha=0.75)

plt.xticks(range(-90,91,30))
plt.yticks(range(-180,181,30))

plt.title("Lat. and Lon. of 'Questionnaire B' with missing values")
plt.xlabel('Latitude')
plt.ylabel('Longitude')

plt.tight_layout()

plt.show()