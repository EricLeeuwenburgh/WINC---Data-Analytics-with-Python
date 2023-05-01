import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%load_ext google.colab.data_table

import pandas as pd
import random
from datetime import datetime, timedelta
from functools import wraps


first_names = [
    "Maria Carmen",
    "Maria",
    "Carmen",
    "Josefa",
    "Isabel",
    "Ana Maria",
    "Maria Dolores",
    "Maria Pilar",
    "Maria Teresa",
    "Ana",
    "Laura",
    "Francisca",
    "Antonia",
    "Dolores",
    "Maria Angeles",
    "Cristina",
    "Marta",
    "Maria Jose",
    "Maria Isabel",
    "Pilar",
    "Maria Luisa",
    "Lucia",
    "Concepcion",
    "Elena",
    "Mercedes",
    "Manuela",
    "Rosa Maria",
    "Raquel",
    "Sara",
    "Maria Jesus",
    "Paula",
    "Juana",
    "Teresa",
    "Rosario",
    "Encarnacion",
    "Beatriz",
    "Rosa",
    "Nuria",
    "Silvia",
    "Montserrat",
    "Julia",
    "Patricia",
    "Irene",
    "Monica",
    "Andrea",
    "Rocio",
    "Angela",
    "Maria Mar",
    "Margarita",
    "Sonia",
    "Sandra",
    "Susana",
    "Alicia",
    "Yolanda",
    "Alba",
    "Maria Josefa",
    "Marina",
    "Natalia",
    "Maria Rosario",
    "Inmaculada",
    "Angeles",
    "Esther",
    "Maria Mercedes",
    "Ana Isabel",
    "Eva",
    "Veronica",
    "Amparo",
    "Noelia",
    "Maria Rosa",
    "Maria Victoria",
    "Maria Concepcion",
    "Carolina",
    "Claudia",
    "Eva Maria",
    "Catalina",
    "Consuelo",
    "Victoria",
    "Lorena",
    "Ana Belen",
    "Maria Antonia",
    "Maria Elena",
    "Miriam",
    "Emilia",
    "Nerea",
    "Luisa",
    "Ines",
    "Maria Nieves",
    "Gloria",
    "Lidia",
    "Carla",
    "Aurora",
    "Esperanza",
    "Josefina",
    "Sofia",
    "Milagros",
    "Olga",
    "Celia",
    "Maria Soledad",
    "Purificacion",
]

store_names = [
    "Situwala",
    "Yakkha",
    "Gnawale",
    "Buhyo",
    "Kutal",
    "Bindukar",
    "Upeti",
    "Mana",
    "Badhyo",
    "Barme",
    "Dhnaju",
    "Kami",
    "Baidhaya",
    "Ma",
    "Ghimere",
    "Sangami",
    "Ghotane",
    "Kewat",
    "Singtan",
    "Chitrakr",
    "Khwaonjoo",
    "Manjhi",
]

city_names = [
    "Távora",
    "Cataguases",
    "Médici",
    "Bressane",
    "Onça",
    "Brígida",
    "Parati",
    "Mônica",
    "Pantano",
    "Anastácio",
    "Ostras",
    "Jequitibá",
]

# Decorate (@) data generating functions to randomly return certain values (decorating = adding to an existing function)
def randomly_return(frequency, value):
    # frequency = 0..1, 0 is return never, 1 is return always
    # value: what to return
    def inner_function(fn):
        @wraps(fn)
        def wrapper():
            return fn() if random.random() > frequency else value
        return wrapper
    return inner_function


@randomly_return(frequency = 0.002, value=np.datetime64('nat'))
def get_datetime_string(min_year=1980, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 0, 0, 0)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

@randomly_return(frequency = 0.003, value=".")
def get_total_amount():
    return round(random.random() * 500, 2)

# Distributed evenly, not realistic.
@randomly_return(frequency = 0.01, value=np.nan)
def get_number_of_products():
    return random.randint(0, 200)

@randomly_return(frequency = 0.07, value="")
def get_cashier():
    return random.choice(first_names)

@randomly_return(frequency = 0.02, value=None)
def get_store_name():
    return random.choice(store_names)

@randomly_return(frequency = 0.07, value="Missing")
def get_city():
    return random.choice(city_names)

@randomly_return(frequency = 0.5, value="NA")
def get_discount_card():
    return random.random() > 0.5

@randomly_return(frequency = 0.006, value=-1)
def get_time_spent():
    return random.randint(30, 600)


def get_random_data(fn, n):
    return [fn() for _ in range(n)]


num_rows = 20_000

data = {
    "datetime": get_random_data(get_datetime_string, num_rows),
    "total_amount": get_random_data(get_total_amount, num_rows),
    "number_of_products": get_random_data(get_number_of_products, num_rows),
    "cashier": get_random_data(get_cashier, num_rows),
    "store": get_random_data(get_store_name, num_rows),
    "city": get_random_data(get_city, num_rows),
    "discount_card_used": get_random_data(get_discount_card, num_rows),
    "time_spent": get_random_data(get_time_spent, num_rows)
}

df = pd.DataFrame(data=data)

## Changing different kind of null values to a default null value
## defaults are: None, NAN (np.nan), NAT (np.nat)

# Three ways of doing this

# 1. Using .loc
# df.loc[df["total_amount"] == ".", "total_amount"] = np.nan  # replacing "." with "NaN"
# print(df.head(20))


# 2. Simple replace .replace(old,new)
# df["total_amount"].replace(".", np.nan, inplace=True)
# print(df.head(20))


# 3. Complex replace
# Simple replace doesn't work when there are None values (empty cells), instead use a dictionary replace:
# .replace({old:new})   
np.sort(df["cashier"].unique()) # inplace argument doesn't work in this case
print(df["cashier"].tail(20))

df["cashier"] = df["cashier"].replace({"": None , np.nan: None})  # inplace argument doesn't work in this case
print(df["cashier"].tail(20))

print(df["cashier"].value_counts(dropna=False))
print(df.loc[df["cashier"].isna()]) # Selects all None values


# Coverting values from different columns to standard null values (in this case: None )
print(df["city"].unique())
df["city"].replace("Missing", None, inplace=True)
print(df["city"].unique())

df["discount_card_used"].unique()
df["discount_card_used"].replace("NA", False, inplace=True)  # Think about what value you replace 'NA' with (False, True)
print(df["discount_card_used"].value_counts())