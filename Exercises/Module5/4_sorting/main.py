import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data_table only "views" certain data, it doesn't save / copy or retain any data
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
    "",
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


def get_total_amount():
  amount = round(random.random() * 500, 2)
  return amount if amount > 5 else np.nan

# Distributed evenly, not realistic.
get_number_of_products = lambda: random.randint(0, 200)

get_cashier = lambda: random.choice(first_names)

get_store_name = lambda: random.choice(store_names)

get_city = lambda: random.choice(city_names)

get_discount_card = lambda: random.random() > 0.5


def get_random_data(fn, n):
    return [fn() for _ in range(n)]


num_rows = 2000

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

print(df)

# Single column
print(df.sort_values(by=['datetime']))

# Ascending/descending
print(df.sort_values(by=['datetime'], ascending=False)) # Default = True

# NaNs at top/bottom
print(df.sort_values(by=['total_amount']))              # Default is last
print(df.sort_values(by=['total_amount'], na_position="first"))

# Use a sorting function
print(df.sort_values(by="cashier", key=lambda cashier: cashier.str.len()))

# Sort by multiple columns
print(df.sort_values(by=['city', 'store']))

# Ascending/descending on multiple columns
print(df.sort_values(by=['city', 'store'], ascending=[False, True]))