# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

language_spain = "Spanish"
language_switzerland = 'Swiss'
print(language_spain == language_switzerland)

religion_spain = "Catholic"
religion_switzerland = "Catholic"
print(religion_spain == religion_switzerland)

capital_spain = "Madrid"
capital_switzerland = "Bern"
print(len(capital_spain) != language_switzerland)

gdp_spain = 1798  #GDP in trillion
gdp_switzerland = 618.228  #GDP in trillion
print(gdp_switzerland > gdp_spain)

population_growth_spain = 0.12  #Growth in percent per year
population_growth_switzerland = 0.64  #Growth in percent per year
print(population_growth_spain < 1 and population_growth_switzerland < 1)

population_count_spain = 47222613
population_count_switzerland = 8563760
print(population_count_switzerland > 10000000 or population_count_spain > 10000000)

print(population_count_spain > 10000000 and population_count_switzerland < 10000000)
