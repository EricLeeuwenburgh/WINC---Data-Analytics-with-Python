import numpy as np
from numpy.random import default_rng

rng = default_rng(1234)
integers = rng.integers(low=-300_000, high=300_000, size=10_000)

print(integers)

# Exercise 1 - What is the highest number in the array?
print("Exercise 1")
print(np.max(integers))

# Exercise 2 - What is the highest number in the array that's lower than 0?
negative_integers = integers < 0
output = integers[negative_integers]
print("Exercise 2")
print(np.max(output))

# Exercise 3 - What is the average of all odd numbers in the array? (odd values are not cleanly divisible by 2)
odd_numbers = integers % 2 == 1
average = np.mean(integers[odd_numbers])
print("Exercise 3")
print(average)

# Complex A - Convert all negative numbers to a positive one. Then subtract 150000 from each value. How many remaining values are positive?
absolute_values = np.abs(integers)
absolute_minus = absolute_values - 150000

remove_negative = absolute_minus > 0
all_positive = absolute_minus[remove_negative]
print("Complex A:")
print(len(all_positive)) # .size also possible on an array

# Complex B - Create a new array. Take the original value, then find the value on the opposite end of the array and subtract that from it. The resulting value is the value in the new array.
#             From the new array, find the smallest number where % 222 == 0.
integers_reversed = integers[::-1] # np.flip() also possible on an array
new_integers = integers - integers_reversed

modulo_222 = new_integers % 222 == 0
new_integers_modulo = new_integers[modulo_222]
print("Complex B:")
print(np.min(new_integers_modulo))

# Youtube
a = np.arange(0, 9).reshape(3,3)
b = np.ones((3,3), dtype=int)

b.fill(5)
print(a, "\n", b)
print(a + b)

