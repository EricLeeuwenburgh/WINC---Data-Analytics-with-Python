# Exercise 1 - Print "Hello World!":
print("Hello World!)")

# Exercise 2 - Add / Sub / Mult / Div numbers:
num1 = 2
num2 = 5

addition = num1 + num2
substraction = num1 - num2
multiply = num1 * num2
divide = num1 / num2

# Exercise 3 - Square root of a number:
import math

print (math.sqrt(9))
print (math.sqrt(25))

# Exercise 4 - Swap two variables:
a = 10
b = 20

#temp =a
#a = b
#b = temp

a , b = b , a

print(a)
print(b)

# Exercise 5 - Print "Hello" 7 times (below eachother):
i = 0
for i in range(7):
    print("Hello")
    i += 1

# Exercise 6 - Generate random number:    
import random

print(random.randint(0,10))

# Exercise 7 - Check if input number is 'odd' or 'even':
def odd_or_even(number):
    if number %2 == 0:
        return "Even"
    else:
        return "Odd"

print(odd_or_even(5))

# Exercise 8 - Find largest number in a list/array:
list = [137,252,7,13,21,56,97,61,151,3]

print(max(list))

# Exercise 9 - Check if a number is a 'prime' or not:
def check_prime(number):
    flag = False

    if check_prime == 1:
        return number, "is not a prime number"
    elif number > 1:
    # check for factors
        for i in range(2, number):
            if (number % i) == 0:
            # if factor is found, set flag to True
                flag = True
            # break out of loop
                break

    # check if flag is True
        if flag:
            return number, "is not a prime number"
        else:
            return number, "is a prime number"

print(check_prime(13))

# Exercise 10 - Check the factorial (example:'5' = 1x2x3x4x5) of any given number:
import math

print (math.factorial(5))

# Exercise 11 - Find the ASCII value of a character:
ascii = 'E'
print("The ASCII value of '" + ascii + "' is", ord(ascii))

# Exercise 12 - Print the current date:
from datetime import date

today = date.today()
print("Today's date:", today)

# Exercise 13 - Perform add, sub, mult, div on two give matrices(matrix):
# Addition;
X = [[1,2,3],
     [4,5,6],
     [7,8,9]]

Y = [[5,8,1],
     [6,7,3],
     [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

# Exercise 14 - Transpose a given matrix:
for k in range(len(X)):
   # iterate through columns
   for l in range(len(X[0])):
       result[l][k] = X[k][l]

for r in result:
   print(r)

# Exercise 15 - Transpose a given matrix: