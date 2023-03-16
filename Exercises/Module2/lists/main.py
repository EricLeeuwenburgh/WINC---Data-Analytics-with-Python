# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# Exercise 1:
def alphabetical_order(film_names):
    film_names.sort()

    return film_names

film_names = ["Mission Impossible", "Jumanji", "The Matrix", "Die Hard", "Jaws"]

print(alphabetical_order(film_names))

# Exercise 2:
def won_golden_globe(film_name):

    film_name = film_name.lower()
    winners = ["jaws", "memoirs of a geisha", "jumanji"]
    
    if film_name in winners:
        return True
    
    else:
        return False

winner = won_golden_globe("Memoirs of a geisha")
print(winner)

# Exercise 3:
def remove_toto_albums(wrong_film_name):
    
    wrong_film_name = wrong_film_name.lower()
    
    if wrong_film_name in film_names:
        film_names.remove(wrong_film_name)
    
    return film_names

film_names = ["Mission Impossible", "old is new", "Jumanji", "The Matrix", "hello world", "Die Hard" , "Jurassic Parc"]

print(remove_toto_albums("Old Is New"))