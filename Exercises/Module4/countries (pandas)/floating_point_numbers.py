import pandas as pd
import numpy as np

# Generate random data for hours and kilometers
hours = np.random.uniform(low=0.0, high=24.0, size=(200,))
kilometers = np.random.uniform(low=0.0, high=50.0, size=(200,))

# Create dataframe
df = pd.DataFrame({'hours': hours, 'kilometers': kilometers})

# Display the top 5 rows of the dataframe 
print(df.head())

### ------------------------------------------------------------------------------------------------------- ###

pd.options.display.float_format = '{:.2f}'.format
print(df)

# iPython 'magics' can't be used directly in VSC (should work in Google Colab), instead use the round() function
# %precision 2
print(df.loc[3,"kilometers"])
print(round(df.loc[3,"kilometers"],2))