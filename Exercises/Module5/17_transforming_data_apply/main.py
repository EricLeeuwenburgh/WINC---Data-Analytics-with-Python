import pandas as pd
import numpy as np

# Let's say we have thermometer measurements but we discover they all
# had an error of measuring 1 degree too low, we can correct like this.

'''

.apply() means applying a function to either columns or rows
.applymap() means applying a function to each element / value of a dataframe

When applying a function to all values in a dataframe it's always better to use: .applymap()

'''

## Apply over each column
# Broadcasting (simple)
temperatures = pd.DataFrame(data={
  "north": [15, 10, 12, 19, -5],
  "east": [18, 12, 20, 10, 7],
  "south": [23, 22, 12, 27, 11],
  "west": [17, 13, 19, 8, 4],
})
print(temperatures)

def add1(col):
  return col + 1

temperatures = temperatures.apply(add1)  # re-assign to original df is needed

print(temperatures)

# Complex
def get_closest_to_average(col):
  average = col.mean()
  smallest_diff = 1000
  for measurement in col:
    if abs(average - measurement) < smallest_diff:
      smallest_diff = abs(average - measurement)
      closest = measurement      
  return closest

print(temperatures.mean())
print(temperatures.apply(get_closest_to_average, axis=0))  # axis=0 == column


## Apply over rows
def get_min_and_max(row):
  return pd.Series([row.max(), row.min()])

print(temperatures)
print(temperatures.apply(get_min_and_max, axis=1))  # axis=1 == row


## Custom functions (like: lambda)
# Named lambda function

add3 = lambda temp: temp + 3

print(temperatures.apply(add3))

# Anonymous inline lambda function
print(temperatures.apply(lambda temp: temp - 2))


## Existing / Built-in functions
temperatures = pd.DataFrame(data={
  "north": [15.12, 10.32, 12.44, 19.01, -5],
  "east": [18, 12.44, 20.65, 10.67, 7.99],
  "south": [23.12, 22.5346, 12.124, 27.2356, 11.19],
  "west": [17.2534, 13.2534, 19.3645, 8.2374, 4.83472],
})

print(temperatures.apply(round))


''' 
Performance:

Using apply can be relatively slow because you do a function call 
for a lot of values and/or pass big datastructures around a lot. 
If you have code that uses apply and you want it to go faster consider 
using other methods of transforming your dataset.

'''