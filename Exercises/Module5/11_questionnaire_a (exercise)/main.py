import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

### Exercise: Visualize the amount of missing values in a dataset

# Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table

# Reading in the dataset
path = "https://raw.githubusercontent.com/WincAcademy/practice_data/main/data/winc/questionnaire_data/qstn-a.csv"
df = pd.read_csv(path)

# Removing the first column
df.drop(columns=["Unnamed: 0"], inplace=True)   # It's best to avoid using index values, like: df.drop(df.columns[0], axis=1, inplace=True)

### (1st findings) Create a vertical bar chart of Null values: One bar for each column (x-axis) and a the number of missing values on the y-axis
null_values = df.isnull().sum()     # Amount of null values per colummn
number_rows = df.shape[0]           # Total rows = 20,000

null_values_percentage = (null_values / number_rows) * 100      # Also possible with .mean() function
above_6_percent = null_values_percentage.loc[null_values_percentage >= 6]

# Setting colors for the bar chart depending on the percentage of null values
colors = ["red" if col in above_6_percent.index else "blue" for col in null_values.index]

# Plot a first graph
plt.figure(figsize=(10, 8))
plt.style.use("fivethirtyeight")

plt.bar(null_values.index, null_values.values, color=colors)

plt.title("Amount of null values in Questionnaire A (per column)\n(without data cleaning)")
plt.xlabel("Column")
plt.ylabel("Number of null values")
plt.xticks(rotation=90, fontsize=8)

blue_patch = mpatches.Patch(color='blue', label='Below 6%') # Manually create handles for the .legend function to plot
red_patch = mpatches.Patch(color='red', label='Above 6%')
plt.legend(handles=[blue_patch, red_patch])

plt.grid(axis="x")
plt.tight_layout()

plt.show()


### Cleaning data

## Finding (the amount of) null values and total values for each column
#print(df.info())                    # General info of all columns

df["resp. id"].info()               # Correct: according .info no null values present
df["datetime"].info()               # Correct: according .info no null values present
df["q1-bool"].unique()              # Correct: only 3 values (True, False, NaN) found
df["q2-lon"].value_counts()         ## Convertion: 0.0 values found which should be converted 
df["q3-id"].unique()                ## Convertion: "no-id" values found which should be converted
df["q4-country"].value_counts()     # Correct: apart from NaN no other values found which should be converted
df["q5-phone_code"].unique()        ## Convertion: values "**" and "***" should be converted
df["q6-number"].value_counts()      # Correct: only numbers and NaN values
df["q7-dt"].isnull().sum()          # Correct: dt-values and NaN: values total == 20000
df["q8-phone_code"].unique()        ## Convertion: values "**" and "***" should be converted
df["q9-currency"].unique()          ## Convertion: values "unknown" should be converted
df["q10-number"].isnull().sum()     # Correct: only numbers and NaN values: values total == 20000
df["q11-dt"].unique()               # Correct: dt-values and NaN: values total == 20000
df["q12-dt"].unique()               # Correct: dt-values and NaN: values total == 20000
df["q13-dt"].unique()               # Correct: dt-values and NaN: values total == 20000
df["q14-lat"].unique()              # Correct: only numbers and NaN values: values total == 20000
df["q15-id"].unique()               ## Convertion: "no-id" values found which should be converted
df["q16-currency"].unique()         ## Convertion: values "unknown" should be converted
df["q17-number"].isnull().sum()     # Correct: only numbers and NaN values: values total == 20000
df["q18-capital"].value_counts()    ## Convertion: "False" values found which should be converted (False in this case is a string (not a Boolean))

# Converting null values to default values (NaN, Nat or None)
df["q2-lon"].replace(0, np.nan, inplace=True)
df["q3-id"].replace("no-id", np.nan, inplace=True) 
df["q5-phone_code"].replace({"**": np.nan, "***": np.nan}, inplace=True)
df["q8-phone_code"].replace({"**": np.nan, "***": np.nan}, inplace=True)
df["q9-currency"].replace("unknown", np.nan, inplace=True) 
df["q15-id"].replace("no-id", np.nan, inplace=True) 
df["q16-currency"].replace("unknown", np.nan, inplace=True) 
df["q18-capital"].replace("False", np.nan, inplace=True)

# Checking if the amount of null values is more than 6 percent 
null_values = df.isnull().sum()     # Amount of null values per colummn
number_rows = df.shape[0]           # Total rows = 20,000

null_values_percentage = (null_values / number_rows) * 100      # Also possible with .mean() function
above_6_percent = null_values_percentage.loc[null_values_percentage >= 6]

# Setting colors for the bar chart depending on the percentage of null values
colors = ["red" if col in above_6_percent.index else "blue" for col in null_values.index]

### (Update) Create a vertical bar chart of Null values: One bar for each column (x-axis) and a the number of missing values on the y-axis
plt.figure(figsize=(10, 8))
plt.style.use("fivethirtyeight")

plt.bar(null_values.index, null_values.values, color=colors)

plt.title("Amount of null values in Questionnaire A (per column)\n(after data cleaning)")
plt.xlabel("Column")
plt.ylabel("Number of null values")
plt.xticks(rotation=90, fontsize=8)

blue_patch = mpatches.Patch(color='blue', label='Below 6%') # Manually create handles for the .legend function to plot
red_patch = mpatches.Patch(color='red', label='Above 6%')
plt.legend(handles=[blue_patch, red_patch])

plt.grid(axis="x")
plt.tight_layout()

plt.show()