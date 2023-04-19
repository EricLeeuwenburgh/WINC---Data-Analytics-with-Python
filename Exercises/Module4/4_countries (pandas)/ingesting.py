import pandas as pd

# pd.read_csv() arguments/parameters:

# sep or delimiter: default = ","
# parse_dates:      turning time, date into data
# thousands:        adjust thousands seperator "." or ","

cali_housing = pd.read_csv("sample_california_housing_test.csv")

print(cali_housing.head())