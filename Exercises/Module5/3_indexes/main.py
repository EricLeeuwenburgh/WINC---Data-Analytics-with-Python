import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

albums = pd.read_csv("../merging_dataframes/albums.csv", sep=";")
print(albums)

# Why mess with indexes?
# 1. natural fit for some datasets (with unique ids)
# 2. easier, more natural access to single rows
# 3. performance

# display(albums)
#print(albums.index)
albums2 = albums.set_index("Album")
#print(albums2)
#print(albums2.index)
#print(albums2.loc['Bad'])
#print(albums2.loc['Bad',['Year of release']])


# inplace and reset_index (inplace means modifying the original dataframe)
albums.set_index("Album", inplace=True)
print(albums)
albums.reset_index(inplace=True)
print(albums)

# sort_index
print(albums2.sort_index())

# set index when reading
pd.read_csv("../merging_dataframes/albums.csv", sep=";", index_col="Album")

# iloc can always be used (select the last three albums)
albums2 = albums.set_index("Album")
print(albums2.sort_index().iloc[-3:])

# slicing with loc
albums2 = albums.set_index("Album")
print(albums2.loc["Bad":"Private Dancer"])