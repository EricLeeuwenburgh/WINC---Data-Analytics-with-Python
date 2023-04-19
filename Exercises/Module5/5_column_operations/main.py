import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%load_ext google.colab.data_table

import random
from datetime import datetime, timedelta

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


def get_datetime_string(min_year=1980, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 0, 0, 0)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


get_total_amount = lambda: round(random.random() * 500, 2)

# Distributed evenly, not realistic.
get_number_of_products = lambda: random.randint(0, 200)

get_cashier = lambda: random.choice(first_names)

get_store_name = lambda: random.choice(store_names)

get_city = lambda: random.choice(city_names)

get_discount_card = lambda: random.random() > 0.5


def get_random_data(fn, n):
    return [fn() for _ in range(n)]


num_rows = 200

data = {
    "datetime": get_random_data(get_datetime_string, num_rows),
    "total_amount": get_random_data(get_total_amount, num_rows),
    "number_of_products": get_random_data(get_number_of_products, num_rows),
    "cashier": get_random_data(get_cashier, num_rows),
    "store": get_random_data(get_store_name, num_rows),
    "city": get_random_data(get_city, num_rows),
    "discount_card_used": get_random_data(get_discount_card, num_rows),
}

df = pd.DataFrame(data=data)

## Dropping columns
print(df)

# Read current columns
print(df.columns)

# Drop single column
print(df.drop(columns='city'))

# Drop multiple columns
print(df.drop(columns=['city','number_of_products','discount_card_used']))

# Immutable by default, use inplace=True to change the original
#df.drop(columns='city', inplace=True)
#print(df)


## Renaming columns

# Simplest method: assigning a list
# Literal values
#print(df.columns)
#new_column_names = ["dt", "total", "num_products", "cashier", "store", "place", "card"]
#df.columns = new_column_names
#print(df)

# We can also generate a list based on df.columns
#print(df.columns)
#new_column_names = [col.split("_")[0] for col in df.columns]
#df.columns = new_column_names
#print(df.columns)

# Or use .str. methods
#print(df.columns)
#new_column_names = df.columns.str.capitalize()
#df.columns = new_column_names
#print(df.columns)
#print(df)


# Or use df.rename to selectively rename columns
#df.rename(columns={"number_of_products": "num_products", "discount_card_used": "card_used"})


## Changing the order of the columns

# We can use loc to (a) select all rows and (b) select all columns but in a different order
df2 = df.loc[:,['discount_card_used','store', 'cashier', 'datetime',  'total_amount', 'number_of_products', 'city']]
print(df2)

# But because we can get the list of columns with df.columns we can also slice and combine that
cols = df.columns.to_list()
print(cols)
new_cols = cols[-3:] + cols[:-3]
print(df.loc[:,new_cols])