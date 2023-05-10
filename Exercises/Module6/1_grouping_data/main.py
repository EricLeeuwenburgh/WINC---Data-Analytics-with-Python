# More info on grouping: 
# https://realpython.com/pandas-groupby/
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

import pandas as pd

df = pd.read_csv('survey_results_public.csv', index_col='Respondent')           # Contains the answers of the survey
schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')        # Contains the questions that were asked in the survey

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df["ConvertedComp"].median()                     # Median = middle value 
df.describe()                                    # Gives a short summary with 'count', 'mean', 'min', 'max'

df["ConvertedComp"].count()                      # Gives the number of non null value rows (not the sum of all values)
df["Hobbyist"].value_counts()                    # Lists the unique values and sums up the total for each value

df["SocialMedia"].value_counts(normalize=True)   # Normalize gives back the percentage instead of the total numbers

#------------------------------------------------------------------------------------------------------------------------------------#

print(df["Country"].value_counts())  

## Group By (splitting / apply function / combine results)
country_grp = df.groupby(["Country"])

print(country_grp.get_group("United States"))                   # Sort survey results by country name
print(country_grp["SocialMedia"].value_counts().head())         # Counts values per country name
print(country_grp["SocialMedia"].value_counts().loc["India"])   # Results of one specific country name

print(country_grp["SocialMedia"].value_counts(normalize=True).loc["Russian Federation"])

#------------------------------------------------------------------------------------------------------------------------------------#

print(country_grp["ConvertedComp"].median().loc["Germany"])     # Median salary in Germany

## Aggregate function (use multiple functions)
print(country_grp["ConvertedComp"].agg(["median", "mean"]))                 # Shows mean and median salary per country
print(country_grp["ConvertedComp"].agg(["median", "mean"]).loc["Canada"])   # Shows results for one country

#------------------------------------------------------------------------------------------------------------------------------------#

filt = df["Country"] == "India"
df.loc[filt]["LanguageWorkedWith"].str.contains("Pyhton").sum()             # Result: Total amount users in India that work with Python  

country_uses_python = country_grp["LanguageWorkedWith"].apply(lambda x: x.str.contains("Python").sum())     # str.contains() doens't work directly with
                                                                                                            # grouped items, therefor .apply is needed
country_respondents = df["Country"].value_counts()

## Concatenate (combine) series
python_df = pd.concat([country_respondents, country_uses_python], axis="columns", sort=False)
python_df.rename(columns={"count": "NumRespondents", "LanguageWorkedWith": "NumKnowsPython"}, inplace=True)     # Rename columns

python_df["PctKnowsPython"] = python_df["NumKnowsPython"] / python_df["NumRespondents"] * 100                   # Get percentage per country
python_df.sort_values(by="PctKnowsPython", ascending=False, inplace=True)

print(python_df.head(50))
print(python_df.loc["Japan"])