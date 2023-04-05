# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# Exercise 1:
def alphabetical_order(film_names):
    film_names.sort()

    return film_names

film_names = ["Jaws", "Indiana Jones", "E.T.", "Schindler's List" , "Jurassic Parc"]

print(alphabetical_order(film_names))

# Exercise 2:
def won_golden_globe(film_name):

    film_name = film_name.lower()
    winners = ["jaws", "memoirs of a geisha", "E.T."]
    
    if film_name in winners:
        return True
    
    else:
        return False

winner = won_golden_globe("Memoirs of a geisha")
print(winner)

# Exercise 3:

movie_names = ["Jaws", "Old Is New", "Indiana Jones", "Hakuna Matata", "E.T.", "Fahrenheit", "Schindler's List", "Jurassic Parc"]
toto_albums = ["Fahrenheit","The Seventh One","Toto XX","Falling in Between","Toto XIV", "Old Is New", "Hakuna Matata"]

def remove_toto_albums(wrong_movie_names):

    for toto_album in toto_albums:
        if toto_album in wrong_movie_names: 
            wrong_movie_names.remove(toto_album)

    wrong_movie_names.sort()
    return wrong_movie_names

print(remove_toto_albums(movie_names))

set = {4,2,3,6.7,3.8}
print(set)