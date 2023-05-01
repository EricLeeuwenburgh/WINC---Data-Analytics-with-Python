import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%load_ext google.colab.data_table

df = pd.read_csv('qstn-b.csv')

# 1. and 2. remove the first column and superfluous lat/lon columns
df2 = df.drop(columns=["Unnamed: 0","q7-lon","q8-lon"])
df2

# Column: "resp. id"
# Let's rename it
df3 = df2.rename(columns={"resp. id": "resp_id"})
df3.shape

def print_separator(sep, num, msg):
  print("\n")
  print(sep * num)
  print(f"{msg}")
  print(sep * num)


def look_at_unique_values(column): 
  unique_values_cutoff = 160
  unique_values = column.unique()
  num_unique_values = len(unique_values)
  if num_unique_values == len(column):
    print(f"Each value in the column is unique (total: {num_unique_values})")
  elif num_unique_values < unique_values_cutoff:
    print(f"Less than {unique_values_cutoff} unique values:")
    # We may get an error when sorting
    try:
      sorted = np.sort(unique_values)
      print("Values are sorted")
      print(list(sorted))
    except:
      print("Could not sort values")
      print(list(unique_values))
  else:
    print(f"More than {unique_values_cutoff} unique values (total: {num_unique_values})")


def look_at_edges(df, column_name):
  # inner function
  def show_head_and_tail(values):
      num_items_to_slice = 10
      print(list(values)[:num_items_to_slice])
      print(list(values)[-num_items_to_slice:])

  column = df[column_name]
  unique_values = column.unique()
  try:
      sorted = np.sort(unique_values)
      print("Unique values sorted, head and tail:")
      show_head_and_tail(sorted)
  except TypeError as error:
      print(f"Could not sort values: {error}")
      print("..so let's try filtering NULL values and then sorting")
      non_null_uniques = df.loc[~df[column_name].isnull(), column_name].unique()
      sorted = np.sort(non_null_uniques)
      show_head_and_tail(sorted)


def cast_to_type(column, maybe_type):
  try:
    column.astype(maybe_type)
    print(f"Casting to {maybe_type} was successful")
  except ValueError as error:
    print(f"Could not cast to {maybe_type}: {error}")


def find_non_default_missing_values(df, column_name, maybe_type):
  long_separator_amount = 80
  short_separator_amount = 40

  print_separator("*", long_separator_amount, f"Finding non default missing values for column \"{column_name}\"")

  print(f"Column \"{column_name}\" has datatype: {df.dtypes[column_name]}")

  column = df[column_name]  

  # A
  print_separator("-", short_separator_amount, "A: Looking at unique values")
  look_at_unique_values(column)

  # B
  print_separator("-", short_separator_amount, "B: Sorting and looking at the edges")
  look_at_edges(df, column_name)

  # C
  print_separator("-", short_separator_amount, f"C: Casting to type: {maybe_type}")
  cast_to_type(column, maybe_type)

  # D
  print_separator("-", short_separator_amount, "D: Looking at frequency")
  print(column.value_counts(dropna=False))

  print("\n")

  # def replace_value(df, column_name, missing_old, missing_new):
  # ⚠️ Mutates df
  # df[column_name] = df[column_name].replace({missing_old: missing_new})

# ✅ resp_id: no missing values
# find_non_default_missing_values(df3, 'resp_id',"string")

# ✅ datetime: no missing values
# find_non_default_missing_values(df3, 'datetime',"datetime64")

# ✅ q1-bool
# replace_value(df3, 'q1-bool', np.nan, False)
# find_non_default_missing_values(df3, 'q1-bool', 'bool')

# ✅ q2-lon
# replace_value(df3, 'q2-lon', 0, np.nan)
# find_non_default_missing_values(df3, 'q2-lon', 'float64')

# ✅ q3-lat: nan, so correct missing value
# find_non_default_missing_values(df3, 'q3-lat', 'float64')

# ✅ q4-country
# replace_value(df3, 'q4-country', np.nan, None)
# find_non_default_missing_values(df3, 'q4-country', 'string')

# ✅ q5-tld
# replace_value(df3, 'q5-tld', "no domain", None)
# replace_value(df3, 'q5-tld', "unknown", None)
# find_non_default_missing_values(df3, 'q5-tld', 'string')

# ✅ q6-bool
# replace_value(df3, 'q6-bool', np.nan, False)
# find_non_default_missing_values(df3, 'q6-bool', 'bool')

# ✅ q9-number: nan, so correct missing value
# find_non_default_missing_values(df3, 'q9-number', 'float64')
df3.sample(10)

# 4. drop all rows that have a missing value for the lat or lon value
df4 = df3.dropna(subset=['q2-lon', 'q3-lat']).copy()

# 5. Sum missing values per row
df4['sum_missing'] = df4.isnull().sum(axis=1)

# # 6. Use only the rows where the number of missing values > 0
df5 = df4.loc[df4['sum_missing'] > 0]
df5

# print(df5)

# 7. make a scatterplot chart
fig, ax = plt.subplots()

x = df5['q3-lat']
y = df5['q2-lon']

ax.scatter(x, y)

plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.title("Lat and lon of questionnaires with missing values.")

fig.set_size_inches(20,10) # Make chart a little bigger

plt.show()