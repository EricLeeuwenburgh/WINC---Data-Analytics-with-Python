from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
# Exercise 1:
def shortest_names(countries):
    
    shortest = min(countries, key=len)
    list_shortest_countries = []

    for country in countries:
        if len(country) == len(shortest):
            list_shortest_countries.append(country)

    return list_shortest_countries    

# Exercise 2:
def most_vowels():


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
# Exercise 1:
print(shortest_names(countries))

# Exercise 2:
print(most_vowels(countries))