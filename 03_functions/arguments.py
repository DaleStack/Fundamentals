"""Arguments and Parameters in Python are used to pass data to functions.
Parameters are the variables defined in the function signature, while arguments are the actual values passed to the 
function when it is called."""


def greet(name):
    """Greet a person with their name."""
    print(f"Hello, {name}!")


greet("Alice")  # 'Alice' is the argument passed to the function


# If you have multiple parameters, you should provide corresponding arguments
def add_numbers(a, b):
    """Add two numbers and print the result."""
    print(a + b)

add_numbers(5, 10)  # 5 and 10 are the arguments
# add_numbers(5)  # This would raise an error because the second argument is missing


"""Default Parameters: You can provide default values for parameters. If an argument is not provided,
the default value is used."""

def power(base, exponent=2):
    print(base ** exponent)

power(3)       # Uses default exponent of 2, prints 9

power(4, 3)   # Overrides default exponent, prints 64


"""Keyword Arguments: You can specify arguments by the parameter name, allowing you to pass them in any order."""

def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person(age=30, city="New York", name="Bob")  # Arguments passed by keyword

"""Positional Arguments vs Keyword Arguments:
Positional arguments are assigned based on their position in the function call, while keyword arguments are assigned 
by parameter name."""



"""Passsing different data types as arguments"""

def display_info(person):
    """Display information about a person."""
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

person_info = {'name': 'Charlie', 'age': 28, 'city': 'Los Angeles'}
display_info(person_info)  # Passing a dictionary as an argument


def list_fruits(fruits):
    """Display a list of fruits."""
    for fruit in fruits:
        print(fruit)

fruit_list = ['Apple', 'Banana', 'Cherry']
list_fruits(fruit_list)  # Passing a list as an argument


"""Return value"""

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

result = multiply(6, 7)
print(f"The result of multiplication is: {result}")

"""Function can return any data type, including lists, dictionaries, or even other functions."""
def create_person(name, age):
    """Create a person dictionary and return it."""
    return {'name': name, 'age': age}

person = create_person("Diana", 25)
print(person)  # Output: {'name': 'Diana', 'age': 25}


"""Positional-Only and Keyword-Only Arguments:"""
def get_info(name, /, age, *, city):
    """Get information about a person."""
    print(f"{name} is {age} years old and lives in {city}.")

get_info("Eve", 22, city="Miami")  # Correct usage
# before / name must be positional
# after * city must be keyword
# get_info(name="Eve", age=22, city="Miami")  # This would raise an error
# get_info("Eve", age=22, "Miami")  # This would raise an error

