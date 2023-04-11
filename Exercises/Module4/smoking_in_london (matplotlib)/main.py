import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype


url = "https://raw.githubusercontent.com/WincAcademy/practice_data/main/data/smoking-indicators.csv"
indicators = pd.read_csv(url, delimiter=";", thousands=",")

# Drop borough id
indicators.drop("la", inplace=True, axis=1)

# Convert to usable arrays
# For chart 1
boroughs = indicators["Borough name"]
smoking_2010_total = indicators["Smoking Status (2010): Total"].to_numpy()

# For chart 2
total = indicators[
    [
        "Borough name",
        "Smoking Status (2010): Total",
        "Smoking Status (2011): Total",
        "Smoking Status (2012): Total",
        "Smoking Status (2013): Total",
    ]
]
# Rename the columns
total.columns = ["boroughs", "2010", "2011", "2012", "2013"]
# Using all the boroughs makes for an illegible chart
total = total[:10]


# Exercise 1 - Horizontal bar chart
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

boroughs = total.loc[:,"boroughs"]
smokers_2010 = total.loc[:,"2010"]

ax.barh(boroughs.iloc[::-1], smokers_2010[::-1]) # reversing order to alpabetical from top to bottom
plt.title("Smokers in London (2010), per borough")
plt.xlabel("Number of smokers")
plt.ylabel("Borough")

#plt.show()


# Exercise 2 - Line chart
fig, ax = plt.subplots()

years = total.columns[1:]

for index, row in total.iterrows():
  plt.plot(years, row[1:], label=row[0])

plt.title("Smokers in London per borough")
plt.xlabel("Year")
plt.ylabel("Number of smokers")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid()

plt.show()