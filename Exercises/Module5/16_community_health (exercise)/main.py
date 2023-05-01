import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly
import pandas as pd
from sklearn.impute import KNNImputer

### Exercise: Use different strategies to drop and fill missing vales. Also visualise the effect of the various strategies.

## Question 1: Is there a relation between the age and number of visits? If so, how are they related?
## Question 2: Is there a relationship between the Body Mass Index (BMI) of a patient and the number of visits? If so, how are they related? 

## Use scatterplots (with lineair regression line) to look for relationships.

# Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table

# Reading in the dataset (patient data on annual docter visits)(weight in "lbs")(height in "inch")
path = "https://raw.githubusercontent.com/WincAcademy/practice_data/main/data/community_health/community_health_missing.csv"
df = pd.read_csv(path)
print(df.head())

# View the mean/average number of missing values per column
# df.info()
print(df.isnull().sum())
print(df.isnull().mean() * 100)

# Dropping any columns we don't need
df.drop(["gender", "race/ethnicity"], axis=1, inplace=True)

### Visualize the relationship between certain data based on different strategies for missing data

## Strategy 1: Keep the missing values as-is
# ''' Do nothing '''

## Strategy 2: Drops rows with any missing data                         # only leaves 22 rows
# df.dropna(inplace=True)                                               

## Strategy 3: Drops rows where we miss data relevant to our questions (age, weight, height, visits)    # leaves 157 rows
# df.dropna(subset=["age", "weight", "height", "visits"], inplace=True) 

## Strategy 4: Replace with literal value ("0")                           # keeps all 1000 rows, but:
# df.fillna(0)                                                            # data gets centered around the value "0"

## Strategy 5: Replace with mean value                                    # keeps all 1000 rows, but:
# df["age"].fillna(df["age"].mean(), inplace=True)                        # gives a lot of values "43.89" 
# df["weight"].fillna(df["weight"].mean(), inplace=True)                  # gives a lot of values "203.83"
# df["height"].fillna(df["height"].mean(), inplace=True)                  # gives a lot of values "67.83"
# df["visits"].fillna(df["visits"].mean(), inplace=True)                  # gives a lot of values "11.37"

## Strategy 6: Replace with median value                                  # keeps all 1000 rows, but:
# fill_values = {"age": df["age"].median(),                               # gives a lot of values "43" 
#                "weight": df["weight"].median(),                         # gives a lot of values "205"
#                "height": df["height"].median(),                         # gives a lot of values "68"
#                "visits": df["visits"].median()}                         # gives a lot of values "11"

# df.fillna(value=fill_values, inplace=True)

## Strategy 7: Replace with mode value                                    # keeps all 1000 rows, but:
# fill_values = {"age": df["age"].mode(),                                 # gives a lot of values "42" 
#                "weight": df["weight"].mode(),                           # gives a lot of values "256"
#                "height": df["height"].mode(),                           # gives a lot of values "68"
#                "visits": df["visits"].mode()}                           # gives a lot of values "10"

# df.fillna(value=fill_values, inplace=True)

## Strategy 8: Interpolate missing values (only for ordered data)         # keeps all 1000 rows, but:
# df["age"].interpolate(method="linear", inplace=True)                    # not usefull here since data isn't ordered
# df["weight"].interpolate(method="linear", inplace=True)                 # not usefull here since data isn't ordered
# df["height"].interpolate(method="linear", inplace=True)                 # not usefull here since data isn't ordered
# df["visits"].interpolate(method="linear", inplace=True)                 # not usefull here since data isn't ordered

## Strategy 9: Use KNN algorithm (dataframe needs to be only numbers in this case, more steps needed for categorical data)
imputer = KNNImputer(n_neighbors=8)     # Creates an instance of the KNNImputer class with k=8 (k generally = between 3 and 10)
df_imputed = imputer.fit_transform(df)     # Imputing the NaN values in df

df_imputed = pd.DataFrame(data=df_imputed, columns=df.columns)    # Converting the imputed values back to a pandas dataframe

## Create BMI column
# Formula BMI (lbs and inch): lbs / (inch^2) x 703
df_imputed["BMI"] = round(df_imputed["weight"] / (df_imputed["height"]**2) * 703, 1)


## Scatterplot 
#plt.style.use("fivethirtyeight")
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

y = df_imputed["visits"]
x1 = df_imputed["age"]
x2 = df_imputed["BMI"]

ax1.scatter(x1, y, color="blue", edgecolor='black', linewidth=1)
ax1.set_title("Age-based")
ax1.set_xlabel("Age")
ax1.set_ylabel("Number of visits")

ax2.scatter(x2, y, color="red", edgecolor='black', linewidth=1)
ax2.set_title("BMI-based")
ax2.set_xlabel("BMI")
ax2.set_ylabel("Number of visits")

ax1.set_xticks(range(0,101,10))
ax1.set_yticks(range(0,31,3))

ax2.set_xticks(range(0,71,10))
ax2.set_yticks(range(0,31,3))

fig.suptitle("Amount of annual doctor visits")
fig.tight_layout()

## Adds the linear regression line (copied from WINC exercise)
# Age-based plot:
try:
    coefs = poly.polyfit(x1, y, 1)
    ffit = poly.polyval(x1, coefs)
    ax1.plot(x1, ffit)

except ValueError as error:
      print(f"Could not plot linear regression line because:{error}")

# BMI-based plot:
try:
    coefs = poly.polyfit(x2, y, 1)
    ffit = poly.polyval(x2, coefs)
    ax2.plot(x2, ffit)

except ValueError as error:
      print(f"Could not plot linear regression line because:{error}")

fig.savefig("KNN.png", dpi=300)
plt.show()