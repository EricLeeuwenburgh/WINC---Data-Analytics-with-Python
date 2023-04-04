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

# Exercise 15 - Sort a list in alphabetic order:
list = ["f","e","z","r","p","b","c","s","a"] 
list.sort()

print(list)

# Exercise 16 - Find most frequent number in list:
list = [1,2,3,4,1,2,3,4,5,2,1,2,1,3,4,2,2,2,2,3,3,3,4,4,4]

def most_frequent(list):
    return max(set(list), key = list.count)

print(most_frequent(list))

# Exercise 17 - Calculte the area of a triangle:
def area_triangle(width, height):
    area = 0.5*width*height

    return area

print(area_triangle(7,10))
# Exercise 18 - Convert Km to Miles:

def km_to_miles(input:float):
    miles = input * 0.621371192

    return miles

print(km_to_miles(10))

# Exercise 19 - Program a calender:
import calendar

yy = 2023  # year
mm = 4    # month

print(calendar.month(yy, mm))

# Exercise 20 - Check if 'leap' year (schrikkel jaar):
def leap_year(year):
    if year % 4 == 0:
        print("It's leap year!")
    else:
        print("It's not leap year.")

leap_year(2023)

# Exercise 21 - Find sum of natural numbers:
def sum_natural_number(number: int) -> int:
    if number < 0:
        print("Enter a positive number")
    else:
        sum = 0
   
    while(number > 0):
       sum += number
       number -= 1
    print("The sum is", sum)

sum_natural_number(16)

# Exercise 22 - Find lowest common multiple of two numbers:
num1 = 12
num2 = 14
for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break
print("LCM of", num1, "and", num2, "is", lcm)

# Exercise 23 - Find highest common factor of two numbers:
num1 = 36
num2 = 60
hcf = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("HCF of", num1, "and", num2, "is", hcf)

# Exercise 24 - Sort words in alphabetic order:
string = "sort the words in this string in alphabetic order."
splitted_string = string.split()
splitted_string.sort()
print(splitted_string)

# Exercise 25 - Sort elements in a list in descending order:
list = ["a", "d,", "b", "s", "z", "p", "o", "c", "f", "h", "u", "l", "n", "k"]
list.sort()
print(list)

# Exercise 26 - Sort elements in a list in ascending order:
list = ["a", "d,", "b", "s", "z", "p", "o", "c", "f", "h", "u", "l", "n", "k"]
list.sort(reverse=True)
print(list)

# Exercise 27 - Generate series of even numbers:
