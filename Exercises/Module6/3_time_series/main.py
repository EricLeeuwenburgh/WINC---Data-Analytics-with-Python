# More info on timeseries: 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior (datetime formats)
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects (date offsets)(resampling data)

import pandas as pd
import matplotlib.pyplot as plt

# Plot chart directly in Google Colab
# %matplotlib line

d_parser = lambda x: pd.to_datetime(x, format="%Y-%m-%d %I-%p")

df = pd.read_csv('ETH_1h.csv')                                              # Contains 1H price data from cryptocurrency Ethereum (ETH) vs US-dollar (USD)
df = pd.read_csv('ETH_1h.csv', parse_dates=["Date"], date_parser=d_parser)  # Convert certain column directly to datetime when reading in the data
print(df.head())

#------------------------------------------------------------------------------------------------------------------------------------#

## Check and convert to 'datetime' datatype 

#df.loc[0, "Date"].day_name()                                       # Gives error, because the current value is a string, not a datetime type
#df["Date"] = pd.to_datetime(df["Date"])                            # Gives error, because string format isn't recognized
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d %I-%p")    # Works by giving in the format of the string

print(df["Date"].head())                    # All values are now converted to 'datetime'
print(df.loc[0, "Date"].day_name())         # Gives back 'Friday'

#------------------------------------------------------------------------------------------------------------------------------------#

## Filter and apply functions on 'datetime' values

df["Date"].dt.day_name()                    # Gives back all day name for entire columns
df["DayOfWeek"] = df["Date"].dt.day_name()  # Creates new column with the day of the week

print(df["Date"].min())                     # Shows oldest date
print(df["Date"].max())                     # Shows latest date
print(df["Date"].max() - df["Date"].min())  # Shows the time 'delta' (time between min and max)

filt = (df["Date"] >= "2019") & (df["Date"] < "2020")   # Filter data on timeseries (year)
print(df.loc[filt])

filt2 = (df["Date"] >= pd.to_datetime("2019-01-01")) & (df["Date"] < pd.to_datetime("2020-01-01"))
print(df.loc[filt2])

df.set_index("Date", inplace=True)          # Converts date column to the new index
print(df.loc["2019"])                       # Gives back all data from 2019

print(df.loc["2020-01":"2020-02"]["Close"]) # Gives back closing prices for 2020 jan. and feb.

print(df.loc["2020-01-01"]["High"].max())   # Highest value for the day

#------------------------------------------------------------------------------------------------------------------------------------#

## Re-sample data (hourly to daily / weekly / etc.)

highs = df["High"].resample("D").max()      # Returns max for each day | D=daily, W=weekly, etc.(see resampling link above for more info)

plt.plot(highs)                             # Show a quick line plot of 'highs'
plt.show()

print(df.resample("W").agg({"Close": "mean", "High": "max", "Low": "min", "Volume": "sum"}))    # Shows a weekly overview of the data