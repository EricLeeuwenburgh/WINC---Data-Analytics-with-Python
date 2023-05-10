import pandas as pd
import numpy as np

### Question: Is there a relation between a country's Gross Domestrict Product (GDP) and its income inequality?

''' 
Some tips:
Be aware of the difference between correlation and causation here. A might cause B. B might cause A. 
But both A and B could be caused by an unknown C as well.

One way to express income inequality is to look at a country's "Gini coefficient" (also known as "Gini index"). 
You can find a dataset of Gini Coefficients here: https://ourworldindata.org/income-inequality#high-income-countries-tend-to-have-lower-inequality

You can find a dataset with historical GDP data here: https://ourworldindata.org/economic-growth#gdp-per-capita-over-the-long-run

To be able to answer this question you would want to calculate the "correlation coefficient" of the GDP and the Gini coefficient. 
But before you can do that you may need to resample the data so a correlation coefficient can be calculated.

More info about calculating correlations using pandas and other Python libraries: https://www.youtube.com/watch?v=TRNaMGkdn-A

'''

# Using datatables in Google Colab 
# %load_ext google.colab.data_table
# pd.options.display.max_columns = 75   # Allows to view more columns (default max = 20)

gini_df = pd.read_csv("economic-inequality-gini-index.csv") 
gdp_df = pd.read_csv("gdp-per-capita-maddison-2020.csv")

print(gini_df)
print(gdp_df) 