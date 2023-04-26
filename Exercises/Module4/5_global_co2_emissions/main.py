import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker  # Needed to modify chart axis to a logarithmic scale

# Read the HTML content of the specified URL and extract any tables found on the page
tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions")

# Select the required table of the read website
countries = tables[2]

# Renaming columns
countries.columns = ["Country", "1990", "2005", "2017", "2021", "2017_world_%", "2017_vs_1990_change", "per_land", "per_capita", "incl_lucf", "excl_lucf"]

# Filtering out the rows containing 'not countries' (like: World and EU)
countries = countries[~countries["Country"].str.contains("World")]          # countries = countries.loc[3:]     Avoid using slicing with index numbers, the website may be updated of changed.
countries = countries[~countries["Country"].str.contains("Europe")]         # countries = countries.drop[67]    It's better to work with 'explicit' values to prevent bugs/errors.

# Removing any unwanted separators (needed for conversion to numeric)
def remove_separator(value):
    if value.count(",") >= 1:
        value.replace(",", "")
    if value.count(".") > 1:
        parts = value.rsplit(".", maxsplit=1)
        return parts[0].replace(".", "") + "." + parts[1]
    else:
        return value

countries.loc[:, "1990": "2021"] = countries.loc[:, "1990": "2021"].applymap(remove_separator)

countries.loc[:, "2017_world_%": "2017_vs_1990_change"] = countries.loc[:, "2017_world_%": "2017_vs_1990_change"].replace("\%", "", regex=True)

# Convert all values to numeric exluding the 'Country'-column
countries.iloc[:, 1:] = countries.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Filtering out the smallest CO2 emitting countries (below 5 Mt)
countries = countries.loc[countries["1990"] > 5]

# Replace NaN values with 0
countries.fillna(value=0, inplace=True)


## Graph 1: Emissions of the 5 biggest CO2 producers

# Select to top 5 countries with the highest emissions in 2021
top_5 = countries.loc[countries["2021"].nlargest(5).index, ["Country", "2021"]]

top_5_data = countries.loc[countries["Country"].isin(top_5["Country"]), ["Country", "1990", "2005", "2017", "2021"]]

# Set the Country column as the index
top_5_data.set_index("Country", inplace=True)

# Transpose the dataframe so that the years become the index and the countries become the columns
top_5_data = top_5_data.transpose()

# Plot the graph
plt.plot(top_5_data)
plt.legend(top_5_data.columns)
plt.xlabel("Year")
plt.xticks([0,1,2,3] ,["1990", "2005", "2017", "2021"])
plt.xticks(rotation=45)
plt.xlim(0, 3)
plt.ylabel("Carbon dioxide emissions (amount in Mt)")
plt.ylim(0, 12500)
plt.title("Top 5 - CO2 Emitting Countries (from 2021)")
plt.grid(True)
plt.show()


## Graph 2: Find the 'top 3' and 'bottom 3' (relative change) countries with regards to lowering their emissions

# New columns for setting relative change percentages since 1990
countries["1990_%"] = (countries.loc[:,"1990"] / countries.loc[:,"1990"]) * 100
countries["2005_%"] = (countries.loc[:,"2005"] / countries.loc[:,"1990"]) * 100
countries["2017_%"] = (countries.loc[:,"2017"] / countries.loc[:,"1990"]) * 100
countries["2021_%"] = (countries.loc[:,"2021"] / countries.loc[:,"1990"]) * 100

# Finding the top 3 and bottom 3 performers (based on 2021)
top_3 = countries.loc[countries["2021_%"].sort_values().nsmallest(3).index, ["Country", "1990_%", "2005_%", "2017_%", "2021_%"]]
bottom_3 = countries.loc[countries["2021_%"].sort_values().nlargest(3).index, ["Country", "1990_%", "2005_%", "2017_%", "2021_%"]]

top_and_bottom_3 = pd.concat([top_3, bottom_3])

# Set the Country column as the index
top_and_bottom_3.set_index("Country", inplace=True)

# Transpose the dataframe so that the years become the index and the countries become the columns
top_and_bottom_3 = top_and_bottom_3.transpose()

# Plot the graph
plt.figure(figsize=(8, 8))
plt.plot(top_and_bottom_3)
plt.legend(top_and_bottom_3.columns)
plt.xlabel("Year")
plt.xticks([0,1,2,3] ,["1990", "2005", "2017", "2021"])
plt.xticks(rotation=45)
plt.xlim(0, 3)
plt.ylabel("Relative amount of CO2 emitted (1990 = 100%)")
# plt.yticks([0,50,100,200,400,800,1600] ,["0%","50%","100%","200%","400%","800%","1600%"])
# plt.ylim(0, 1600)

plt.yscale("log")

def to_percent(y, _):
    return '{:.0f}%'.format(y)

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(to_percent))
plt.yticks([10, 50, 100, 200, 400, 800, 1600], ['10%', '50%', '100%', '200%', '400%', '800%', '1600%'])

# Code above starting from .yscale is to make the y-axis logarithmic. 

plt.title("The 3 best and 3 worst performing\ncountries (change in % CO2 emission)")
plt.grid(True)
plt.show()