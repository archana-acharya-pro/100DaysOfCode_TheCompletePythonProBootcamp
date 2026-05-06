# Write your code below this line 👇

# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"What is it like in {location}")


greet_with("Jack Bauer", "Orlando") # Positional argument,  Parameter is the name of the variable in function.
greet_with(location="Orlando", name="Archana") # Keyword arguments.  Argument is the value passed to function.
greet_with(name="Jack Bauer", location="Orlando") # Keyword arguments
