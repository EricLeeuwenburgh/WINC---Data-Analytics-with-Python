# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    return (f"Hello, {name}!")

print(greet("Eric"))

def add(nr_1,nr_2,nr_3):
    return nr_1 + nr_2 + nr_3

print(add(1.5,2,3))

def positive(number):
    return number > 0

print(positive(25))
print(positive(-25))

def negative(number):
    return number < 0

print(negative(5))
print(negative(-5))