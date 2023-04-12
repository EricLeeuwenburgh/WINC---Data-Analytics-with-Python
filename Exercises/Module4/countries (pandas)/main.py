import pandas as pd

tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_birth_rate")
countries = tables[0]
print(countries)

