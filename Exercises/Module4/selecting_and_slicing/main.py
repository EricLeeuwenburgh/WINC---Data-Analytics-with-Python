import numpy as np
from numpy.random import default_rng

rng = default_rng(1234)

mystery_array = (rng.integers(low=0, high=500, size=216)
                * rng.integers(low=0, high=500, size=216)
                ).reshape((6, 6, 6))

print(mystery_array)

# The following should be: numpy.int64
# type(your_selection)

print(mystery_array[0,0,0])
print(mystery_array[5,5,5])
print(mystery_array[2,5,2])
print(type(mystery_array[2,5,2]))

# Exercise 1
one = mystery_array[4,5]
print(one)

# Evercise 2
print(mystery_array[0,2,3:])

# Evercise 3
print(mystery_array[4,:,4])
