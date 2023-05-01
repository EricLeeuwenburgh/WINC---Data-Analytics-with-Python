import pandas as pd
import numpy as np

# Extra info
# Wiki imputation: https://en.wikipedia.org/wiki/Imputation_(statistics)
# Multiple imputation: https://stefvanbuuren.name/fimd/sec-nutshell.html
# Manual and visual processing of missing data: https://www.youtube.com/watch?v=qIXHLZJJ42U
# Manual and visual explanation for multiple imputation: https://www.youtube.com/watch?v=LMsULWGtP2c
# Imputation using scikit library: https://scikit-learn.org/stable/modules/impute.html
# Wiki K:nearest neighbors algorithm: https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
# Visual explanotion of the KNN algorithm: https://www.youtube.com/watch?v=HVXime0nQeI

## Imputation = assigning values to cells where data is missing. Note that imputation may cause a certain bias!
## Single imp. = assign one value to a missing cell
## Multiple imp. = (temporarily) assigning multiple values to a missing cell, do analysis based on these values and take the best result as actual value

nan = np.nan

df = pd.DataFrame(data={
    "age": [nan,29,29,32,95],
    "height_cm": [180,190, 180, nan, 155],
    "weight_kg": [80, 80, nan, 90, 45],
},dtype=np.float64)
print(df)

# Same value everywhere
df.fillna(0)

# Fill with mean (average)
print(df)
print(df.mean())
df.fillna(df.mean())

# Fill with median (center value)
print(df)
print(df.median())
df.fillna(df.median())

# Fill with mode (most frequent number)
print(df)
print(df.mode()) # Returns a new df (not a series), so we need to grab the first and only row
df.fillna(df.mode().iloc[0])

# Interpolation (looing at neighbour values and take the average of those: not useful in this case because ordering is irrelevant)
print(df)
print((180 + 155) / 2)
print((80 + 90) / 2)
df.interpolate(method="linear")

# ffill/bfill (forward- and backward-fill: not useful in this case)
print(df)
df.fillna(method='ffill')
# df.fillna(method='bfill')

# Hot deck method (looking a similar rows and filling based on that data)
# Used in 70's/80's a lot. Not recommended anymore because it adds more bias than newer methods.

# K Nearest Neighbour (algorithm: looks a similar mulitple rows/data and fills based on that)
print(df)

from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=2)
imputed = imputer.fit_transform(df)
print(imputed)

pd.DataFrame(data=imputed, columns = ["age", "height", "weight", "visits"])