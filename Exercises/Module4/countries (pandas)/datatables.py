import pandas as pd
import numpy as np

# Create a datetime range for the 'datetime' column
date_rng = pd.date_range(start='1/1/2020', end='1/08/2020', freq='H')

# Create a DataFrame with 200 rows and 7 columns
df = pd.DataFrame(columns=['datetime', 'total_amount', 'number_of_products', 'cashier', 'store', 'city', 'discount_card_used'], index=range(200))

# Fill the DataFrame with random data
df['datetime'] = np.random.choice(date_rng, size=len(df))
df['total_amount'] = np.random.uniform(low=10, high=1000, size=len(df))
df['number_of_products'] = np.random.randint(low=1, high=10, size=len(df))
df['cashier'] = np.random.choice(['John', 'Mary', 'Bob', 'Alice'], size=len(df))
df['store'] = np.random.choice(['Store A', 'Store B', 'Store C'], size=len(df))
df['city'] = np.random.choice(['New York', 'London', 'Paris', 'Tokyo'], size=len(df))
df['discount_card_used'] = np.random.choice([True, False], size=len(df))

# reset the index to avoid the ValueError
df = df.reset_index(drop=True)

# display the dataframe
#print(df)

### ------------------------------------------------------------------------------------------------------- ###

# Google Colab command:
# %load_ext google.colab.data_table

# Whenever showing the dataframe after this code you get a new GUI. Looks like excel with filters.
# Note that this extension may not work when your dataframe has more the 20 columns.