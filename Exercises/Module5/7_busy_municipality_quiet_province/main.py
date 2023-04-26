import pandas as pd
import matplotlib.pyplot as plt

# Read all files directly from GitHub
path = "https://raw.githubusercontent.com/WincAcademy/practice_data/main/data/geo/municipalities/"
files = ["drenthe.csv", 
         "flevoland.csv", 
         "friesland.csv", 
         "gelderland.csv", 
         "groningen.csv", 
         "limburg.csv", 
         "noord-brabant.csv", 
         "noord-holland.csv", 
         "overijssel.csv", 
         "utrecht.csv", 
         "zeeland.csv", 
         "zuid-holland.csv"]

columns_mun = ["Municipality", "Province", "Inhabitants", "Surface Area in sq km"]
columns_prov = ["province", "inhabitants", "surface_sq_km"]

municipalities_list = [pd.read_csv(path + file, usecols=columns_mun) for file in files]
provinces = pd.read_csv("https://raw.githubusercontent.com/WincAcademy/practice_data/main/data/geo/provinces.csv", usecols= columns_prov)

# Concatenate all municipalities into one dataframe
municipalities = pd.concat(municipalities_list) 

# Renaming columns
municipalities.rename(columns={"Surface Area in sq km": "surface_sq_km"}, inplace=True)
municipalities.columns = municipalities.columns.str.lower()

# Calculate inhabitant density 
municipalities["density"] = municipalities["inhabitants"] / municipalities["surface_sq_km"]
provinces["density"] = provinces["inhabitants"] / provinces["surface_sq_km"]

# Renaming columns for merge
municipalities.rename(columns={"inhabitants": "inhabitants_mun", "surface_sq_km": "sq_km_mun", "density": "density_mun"}, inplace=True)
provinces.rename(columns={"inhabitants": "inhabitants_prov", "surface_sq_km": "sq_km_prov", "density": "density_prov"}, inplace=True)

# Merge the dataframes
merged_df = pd.merge(municipalities, provinces, on="province")

# Calculate the relative density between municipality and province
merged_df["relative_density"] = merged_df["density_mun"] / merged_df["density_prov"]

# Sort the dataframe basic on relative density
merged_df.sort_values(by="relative_density",ascending=False, inplace=True)

# Select the top 10 (highest density)
top_10 = merged_df.head(10)
print(top_10)

# Create a plot (hor.bar) with municipalities on the y-axis and the relative density on the x-axis
plt.figure(figsize=(20, 10))

y = top_10["municipality"][::-1]
x = top_10["relative_density"][::-1]

plt.barh(y, x)
plt.xlabel("Relative density")
plt.xticks(range(11))
plt.ylabel("Municipalities")
plt.title("Top 10 - Most dense municipalities (relative to their province)")
plt.grid(axis="x")

plt.show()


