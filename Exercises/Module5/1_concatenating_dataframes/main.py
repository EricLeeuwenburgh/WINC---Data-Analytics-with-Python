import os
import matplotlib.pyplot as plt
import pandas as pd

## SUPERMARKET FILES NOT PROVIDED - SO CAN'T RUN THIS CODE ##

# Read in one file
df = pd.read_csv("./supermarket_0.csv", parse_dates=['datetime'])
df = df.sort_values(by=["datetime"])
# display(df) 
# display(df.dtypes)


def make_chart(df):
  # group by year
  grouped = df.groupby(df.datetime.dt.year)
  summed_sales = grouped.sum()

  # make chart  
  fig,ax = plt.subplots()
  years = summed_sales.index
  total_sales = summed_sales.loc[:,["total_amount"]]
  plt.plot(years, total_sales)
  plt.title("Sales per year")
  plt.xlabel("Year")
  plt.ylabel("Total sales per year")
  plt.grid()
  plt.show()


make_chart(df)

# Select all file ending with .csv in current folder
path = "."
files = [file for file in os.listdir(path) if file.endswith(".csv")] # Ignore hidden files
# display(files)

all_dfs = [pd.read_csv(file,parse_dates=['datetime']) for file in files]
# display(all_dfs)

all = pd.concat(all_dfs)
# display(all)
make_chart(all)