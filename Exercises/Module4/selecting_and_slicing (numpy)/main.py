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

# Youtube
a = np.zeros((3,3), dtype = np.int64)
a[:] = 2
a.fill(8)
a += 3
print("Array A\n", a)

b = np.arange(1, 10).reshape((3,3))
print("Array B\n", b)

sum = b.sum(axis=1)
print(sum)

mean = b.mean()
print(mean)

min_and_max_index = b.argmin(), b.argmax()
print(min_and_max_index)

# flatten array
array_flat = b.reshape(b.size)
array_flat = b.flatten()

print(array_flat)

# repeat values/arrays and inverse
array_repeat = np.repeat(b, 3, axis=0)
print(array_repeat)
array_unique = np.unique(array_repeat, axis=0)
print(array_unique)
array_diagonal = np.diagonal(b, offset=0)
print(array_diagonal)

# write array to a file
b.tofile("my_array.txt", sep=",")