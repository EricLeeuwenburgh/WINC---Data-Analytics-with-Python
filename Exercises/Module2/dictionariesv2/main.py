# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

# Exercise 1:
def create_passport(name:str, date_of_birth:str, place_of_birth:str, height:float, nationality:str):  # Example date_birth = 2002-12-31

    passport = {"name": "1", "date_of_birth": "2", "place_of_birth": "3", "height": 4.0, "nationality": "5"}

    passport["name"] = name
    passport["date_of_birth"] = date_of_birth
    passport["place_of_birth"] = place_of_birth
    passport["height"] = height

    for country in get_countries():
        if nationality == country:
            passport["nationality"] = country
    
    return passport


# Exercise 2:
def add_stamp(passport, stamp):

    if "stamps" not in passport and stamp != passport["nationality"]:
        passport["stamps"] = stamp
    elif stamp == passport["nationality"]:
        passport["stamps"] = passport["stamps"]
    elif stamp in passport["stamps"]:
        passport["stamps"] = passport["stamps"]
    else:
        passport["stamps"] = [passport["stamps"], stamp]

    return passport

# Exercise 3:
def add_biometric_data(passport, bio_type, bio_value, bio_date):

    if "biometric" not in passport:
        passport["biometric"] = {}

    biometric_data = {"value": bio_value, "date": bio_date}
    passport["biometric"][bio_type] = biometric_data
    
    return passport

# -- See code from teacher above, much cleaner better to start with an empty list/dictionary and fill it afterwards --
# if "biometric" not in passport:
#    passport["biometric"] = {bio_type:{"value": bio_value, "date": bio_date}}

# elif "biometric" in passport:
#    if bio_type in passport["biometric"]:
#       passport["biometric"][bio_type] = {"value": bio_value, "date": bio_date}
# 
# else:
#    passport["biometric"] = passport["biometric"], {bio_type:{"value": bio_value, "date": bio_date}}
#              
#    return passport


# Exercise 1:
passport = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")


# Exercise 2:
#passport  = add_stamp(passport, "Germany")
#passport = add_stamp(passport, "Jemen")
#passport = add_stamp(passport, "Netherlands")
#passport = add_stamp(passport, "Germany")


# Exercise 3:
passport = add_biometric_data(passport, "eye_color_left", "blue", "2020-05-05")
passport = add_biometric_data(passport, "eye_color_right", "blue", "2020-05-05")
print(add_biometric_data(passport, "eye_color_left", "brown", "2022-01-10"))

