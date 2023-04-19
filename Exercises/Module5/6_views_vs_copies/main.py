import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://github.com/WincAcademy/practice_data/raw/main/data/random_data_set/sample.csv"
df = pd.read_csv(url, usecols = ['datetime','total_amount','cashier','store','city'])
#print(df)

## VIEW
# All amounts for Dolores need to be increased by 10 percent
dolores_mask = df.cashier == "Dolores"
#print(df.loc[dolores_mask])

#df.loc[dolores_mask, 'total_amount'] = df.loc[dolores_mask, 'total_amount'] * 1.1
#print(df.loc[dolores_mask])

## COPY
# All amounts for Dolores need to be increased by 10 percent
dolores_mask = df.cashier == "Dolores"
#print(df.loc[dolores_mask])

# ⚠️ chaining creates a copy (WARNING != ERROR)
df[dolores_mask]['total_amount'] = df.loc[dolores_mask, 'total_amount'] * 1.1
df.loc[dolores_mask].total_amount = df.loc[dolores_mask, 'total_amount'] * 1.1
print(df.loc[dolores_mask])

# Use .copy()
# All amounts for Dolores need to be increased by 10 percent
dolores_mask = df.cashier == "Dolores"
#print(df.loc[dolores_mask])

# Use copy
df_dolores = df.loc[dolores_mask].copy()
# df_dolores.loc[:,'total_amount'] = df_dolores.loc[:, 'total_amount'] * 1.1
# df_dolores.total_amount = df_dolores.total_amount * 1.1
df_dolores.total_amount *= 1.1

#print(df_dolores)
#print(df.loc[dolores_mask])