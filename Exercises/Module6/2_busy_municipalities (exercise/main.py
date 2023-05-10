import pandas as pd

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

municipalities_list = [pd.read_csv(path + file, usecols=columns_mun) for file in files]

#------------------------------------------------------------------------------------------------------------------------------------#

## Concatenate (combine) all municipalities into one dataframe
municipalities = pd.concat(municipalities_list)
print(municipalities)

#------------------------------------------------------------------------------------------------------------------------------------#

## Calculate the busiest and the least busy municipality per province using groupby
municipalities["Inhab per sq km"] = municipalities["Inhabitants"] / municipalities["Surface Area in sq km"]

grp_mun = municipalities.groupby(["Province"])      # Group results by "Province"

print("Top 3 - Most busy municipalities per province:")
top_mun_prov = grp_mun.apply(lambda x: x.nlargest(n=3, columns="Inhab per sq km"))      # Selects the 3 largest from column
print(top_mun_prov)

print("Bottom 3 - Least busy municipalities per province:")
bottom_mun_prov = grp_mun.apply(lambda x: x.nsmallest(n=3, columns="Inhab per sq km"))  # Selects the 3 smallest from column
print(bottom_mun_prov)