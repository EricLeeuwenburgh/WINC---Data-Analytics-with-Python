# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Assignment 1:
def greet(name:str, template:str=f"Hello, <name>!") -> str:
    greet = template.replace("<name>", name)
    return greet

print(greet("Eric"))
print(greet("Eric", "What's up, <name>!"))


# Assignment 2:
def force(mass: float, body: str="Earth") -> str: # mass in Kg & force in Newton

    planets = {"sun": 274, "jupiter": 24.92, "neptune": 11.15, "saturn": 10.44, "earth": 9.798, "uranus": 8.87, "venus": 8.87, "mars": 3.71, "mercury": 3.7, "moon": 1.62, "pluto": 0.58} 
    
    gravity = planets.get(body.lower())
    gravity_rounded = round(gravity,1)
    force = mass * gravity_rounded
    return force

print(force(10.1))
print(force(10.1,"Mars"))
print(force(10.1,"Earth"))
print(force(10.1,"Sun"))


# Assignment 3:
def pull(m1:float, m2:float ,d:float) -> float: # distance in Meters
    gravitational_constant = 6.674*(10**-11)
    pull = gravitational_constant * ((m1*m2)/d**2)
    return pull

print(pull(800,1500,3))