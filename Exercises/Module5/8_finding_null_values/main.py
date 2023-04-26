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

# Decorate data (@) generating functions to randomly return certain values (decorate = adding to existing functions)
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
#print(df)

## Use .isnull/.isna on series or dataframes to find "default" null values: None, NaN, NaT
mask_of_null_values = df.loc[:,'store'].isnull()
print(df.loc[:,'store'].isnull().sum())

# Get the percentage
missing_stores = df.loc[:,'store'].isnull().sum()
total_rows = df.shape[0]
percentage = round((missing_stores / total_rows) * 100,3)
print(f"The percentage of missing values for column 'store' is {percentage}%.")


## Second example: with null value = NaN
# df.loc[:,'number_of_products'].isnull()
df.loc[:,'number_of_products'].isnull().sum()

# Get the percentage
missing_number_of_productss = df.loc[:,'number_of_products'].isnull().sum()
total_rows = df.shape[0]
percentage = round((missing_number_of_productss / total_rows) * 100,3)
print(f"The percentage of missing values for column 'number_of_products' is {percentage}%.")


## But now let's look at another column: "discount_card_used" ('NA' isn't a default null-value)
# df.loc[:,'discount_card_used'].isnull()
print(df.loc[:,'discount_card_used'].isnull().sum()) # returns '0'

# The reason for this: isnull() only recognizes a small selection of NULL values: None, NaN, NaT
# So how can we find the other ones?

## 1. Looking at all the unique values

# For columns with a small amount of different values we can look at all the unique values
print(df.loc[:,'discount_card_used'].unique())

# df['discount_card_used'] == 'NA'
(df['discount_card_used'] == 'NA').sum()

# We also could have found this with method 3: casting

# Second example
print(df.loc[:,'city'].unique())

df['city'] == 'Missing'
(df['city'] == 'Missing').sum()


## 2. Sorting and looking at the edges

# For columns with larger amount of different values
sorted = df.loc[:,'cashier'].sort_values()
print(sorted.head())
print(list(sorted.head())) # returns Empty strings
print(sorted.tail())

df.loc[:,'cashier'].unique()


# Sorting and looking at the edges, with LOTS of different values
# Datetime
print(len(df.loc[:,'datetime'].unique())) # return != 20000 which means there are null values present
sorted = df.loc[:,'datetime'].sort_values()
print(sorted.head())
print(sorted.tail()) # return several NAT values (Not a Time)

# But luckily this NaT is one of the default null values panda can recognize with .isnull
print(df.loc[:,'datetime'].isnull().sum())


## 3. casting to a type

# Let's look at another column "total_amount"
# total_amount_sorted = np.sort(df.loc[:,'total_amount'])   # error = operator ">" not supported between type 'str' and 'float'
# df.sort_values(by="total_amount")                         # Other way of sorting, same error
# print(total_amount_sorted[0:10])
# print(total_amount_sorted[-10:])

# Let's look at all the types of our columns
print(df.info())

# We can cast some columns to see if/when the casting breaks
# df.loc[:,'total_amount'].astype('float')                    # error = could not convert string to float '.'
# If there are multiple missing value values you may need to do this multiple
# times.

# More on casting columns later!


## 4. Looking at the frequency

# We can use value_counts on a Series to get the frequency of each value
print(df.loc[:,'time_spent'].value_counts())

# But: there's a bigger chance we would've found this by sorting.
# If the frequency of -1 was different we maybe would not have found it.

"""
General process for missing values

When you come across missing values in your dataset the general process is this:

convert missing values to NULL values
analyze amount and pattern of missing values
delete or "impute" them
To do these things you'll want to:

find missing values
convert them to "proper" NULL values
view the missing values in various ways (single rows or summarized in various ways)
optionally visualize the missing values
know various ways of deleting values
know various ways of replacing a missing value with an actual value
"""