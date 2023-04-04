# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
# Exercise 1
import this
import time
import math
import datetime
import sys
from greet import supergreeting

# Exercise 2
def wait(seconds:int):
    print(f"Waiting {seconds} second(s) before continuing") 
    time.sleep(seconds)


wait(1)

# Exercise 3
def my_sin(input:float):
    sin = (math.sin(input))
    return sin

print(my_sin(5.50))

# Exercise 4
def iso_now() -> str:
    date_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    return date_time


print(iso_now())

# Exercise 5
def platform() -> str:
   return sys.platform
   

print(platform())

# Exercise 6
def supergreeting_wrapper(name):
    greet = supergreeting(name)
    return greet

print(supergreeting_wrapper("Eric"))


