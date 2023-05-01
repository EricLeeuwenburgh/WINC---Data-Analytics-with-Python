import pandas as pd
import numpy as np

# Transform - broadcasting

# Let's say we have thermometer measurements but we discover they all
# had an error of measuring 1 degree too low, we can correct like this.

temperatures = pd.DataFrame(data={
  "north": [15, 10, 12, 19, -5],
  "east": [18, 12, 20, 10, 7],
  "south": [23, 22, 12, 27, 11],
  "west": [17, 13, 19, 8, 4],
})

def add1(col):
  return col + 1

print(temperatures.transform(add1))

# Transform - complex (passing a function)
def deviation_from_average(col):
  average = col.mean()
  return abs(col - average)

print(temperatures.transform(deviation_from_average))

### Transform - passing a string, list or dictionary
print(temperatures.transform('round'))

'''
Passing a string:
Pandas can "find" these functions by looking at the methods attached to the Series or DataFrame you're calling transform on. It also checks all NumPy functions. 
If it can't find a function with that name in either place you'll get an error.

Passing a list:
The first argument to transform can be a function, a string, a list or a dictionary.
If we pass a list the items in the list can be strings or functions. If they're strings pandas looks for functions with that name. So ultimately we end up with a list of functions.
What happens then is that each function is applied to each value in the column in parallel. So not sequentially (one after the other). The end result is a so-called MultiIndex dataframe where each previous column now has a "sub-column" per function in the list.
MultiIndex dataframes are a whole topic by themselves which we'll not cover in this lesson.
Passing a list to transform can be useful if you want to apply and end up with multiple transformations of the same value in a column (or row).

Passing in a dictionary:
If we pass in a dictionary we can perform specific transformations on specific columns and leave out certain other columns from the result.
The keys of the dictionary we pass in determine which columns we'll be transforming. The values of the corresponding dictionary keys determine which transformation(s) will be applied to the columns.

'''
# Applying a list

def deviation_from_average_per_region(col):
  average = col.mean()
  return abs(col - average)

def deviation_from_average_overall(col):
  # Calculating this over and over again is not very efficient.
  # We could pass it as an argument instead.
  overall_mean = temperatures.mean().mean()
  return abs(col - overall_mean)


## Create a MultiIndex dataframe (one column for each function applied)
# Creates extra columns
print(temperatures.transform([deviation_from_average_per_region, deviation_from_average_overall]))


# Creates extra rows
def deviation_from_average_per_moment(row):
  average = row.mean()
  return abs(row - average)

def deviation_from_average_overall(row):
  # Calculating this over and over again is not very efficient.
  # We could pass it as an argument instead.
  overall_mean = temperatures.mean().mean()
  return abs(row - overall_mean)

def original(series):
  return series

print(temperatures.transform([original, deviation_from_average_per_moment, deviation_from_average_overall], axis=1))


# Applying a dictionary

# Let's say we have a list of products in a dataframe. We want to capitalize the
# product name and at the same time increase the price with 10% and round it.

sales = pd.DataFrame(data={
  "product_name": ["tofu", "tempeh", "seitan", "jackfruit", "banana flower"],
  "price": [23, 22, 12, 27, 11],
  "barcode": ["ABC", "CDE", "EFG", "GHI", "JKL"]
})

print(sales)

print(sales.transform({"product_name": str.capitalize, "price": lambda price: round(price * 1.1)}))

# Multiple transformations per column
def old_price(price):
  return price

def new_price(price):
  return round(price * 1.1)

def price_before_vat(price):
  # VAT == value added tax
  return round(price / 1.19)


print(sales.transform({"product_name": str.capitalize, "price": [old_price, new_price, price_before_vat]}))