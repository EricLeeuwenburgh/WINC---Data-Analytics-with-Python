import pandas as pd
import numpy as np

# No missing values
df = pd.DataFrame(data={
    "col1": [1,2,3],
    "col2": [4,5,6],
    "col3": [7,8,9],
},dtype=np.int8)
print(df)

# Drop rows with 1 or more missing values
df = pd.DataFrame(data={
    "col1": [1,2,3],
    "col2": [4,5,np.nan],
    "col3": [7,np.nan, np.nan],
}).dropna()
print(df)

# Drop rows where all values are missing
df = pd.DataFrame(data={
    "col1": [1,2,np.nan],
    "col2": [4,5,np.nan],
    "col3": [np.nan, np.nan, np.nan],
}).dropna(how="all")
print(df)

# Drop rows where "any" value from col1 or col2 are missing
df = pd.DataFrame(data={
    "col1": [1,2,3],
    "col2": [4,np.nan,6],
    "col3": [7,8,np.nan],
}).dropna(subset=['col1', 'col2'])
print(df)

# Drop rows where "all" values from col1 or col2 are missing
df = pd.DataFrame(data={
    "col1": [np.nan,np.nan,3],
    "col2": [4,np.nan,6],
    "col3": [7,8,np.nan],
}).dropna(subset=['col1', 'col2'], how="all")
print(df)