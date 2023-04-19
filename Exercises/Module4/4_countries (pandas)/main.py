# Import the pandas library with an alias 'pd'
import pandas as pd

# Read the HTML content of the specified URL and extract any tables found on the page
tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_birth_rate")

# Since we know that the table we want is the first one on the page, we access it by indexing into the 'tables' list with [0]
countries = tables[0]

# Print out the 'countries' table to the console
#print(countries)

# Renaming columns
countries.columns = ["Country", "WB2018", "OECD2011", "CIA2013", " CIA2014", "CIA2020", "PRB2022"]


## Exercise 1 - Select all countries but not the dependent territories
filtered_countries = countries.loc[:195,:]

# Alternative: setting index column to the Country column
# countries_new_index = countries.set_index("Country")
# print(countries_new_index.loc[:"Zimbabwe",:])


## Exercise 2 - Select all countries with a birthrate over 40 according PRB
PRB_above_40 = filtered_countries.loc[:,"PRB2022"] > 40

filtered_countries2 = filtered_countries.loc[:, ["Country", "PRB2022"]]

print(filtered_countries2[PRB_above_40])

# Solution:
# print(filtered_countries.loc[countries.PRB2022 > 40,["Country", "PRB2022"]])


## Exercise 3 - Select all countries with "stan" in their name and with a birthrate below 25 according CIA 2020
contain_stan_below_25 = filtered_countries[filtered_countries["Country"].str.contains("stan") & (filtered_countries["CIA2020"] < 25)]
filtered_countries3 = contain_stan_below_25.loc[:, ["Country", "CIA2020"]]

print(filtered_countries3)

# Solution:
# stan_mask = filtered_countries.country.str.contains("stan")
# below_25_mask = countries.CIA2020 < 25
# print(filtered_countries.loc[stan_mask & below_25_mask, ["Country", "CIA2020"]])


## Exercize 4 - Select all countries where the birth rate dropped more than 7 percent between 2013 and 2020 according CIA
drop_7_percent_or_more = filtered_countries[filtered_countries["CIA2013"] - filtered_countries["CIA2020"] > 7]
filtered_countries4 = drop_7_percent_or_more.loc[:,["Country", "CIA2013","CIA2020"]]

print(filtered_countries4)

# Alternative: Using lambda
# filtered_countries4 = filtered_countries.loc[:,["Country", "CIA WF 2013","CIA WF 2020"]]
# filtered_countries4 = filtered_countries4[filtered_countries4.apply(lambda row: row['CIA2020'] / row['CIA2013'] < 0.93, axis=1)]
# print(filtered_countries4)

# Solution:
# def dropping_birth_rate(country):
#   drop = country.CIA2013 - country.CIA2020
#   return drop > 7
# print(filtered_countries.loc[lambda country:dropping_birth_rate(country), ["Country", "CIA2013", "CIA2020"]])