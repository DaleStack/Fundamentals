""" *args and **kwargs in python are used to pass a variable number of arguments to a function."""

# *args allows you to pass a variable number of non-keyword arguments to a function. This will be received as a tuple.
# **kwargs allows you to pass a variable number of keyword arguments to a function. This will be received as a dictionary.


"""Regular parameters must be defined before *args and **kwargs in the function definition."""
def display_args(*args):
    """Display all positional arguments passed to the function."""
    for index, value in enumerate(args):
        print(f"Argument {index}: {value}")
    print(args)

display_args(1, 2, 3, "hello", True)  # Passing multiple positional arguments



def display_kwargs(**kwargs):
    """Display all keyword arguments passed to the function."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(kwargs)

display_kwargs(name="Alice", age=30, city="New York")  # Passing multiple keyword arguments

def display_all(a, b, *args, **kwargs):
    """Display regular parameters, *args, and **kwargs."""
    print(f"a: {a}, b: {b}")
    print("Positional arguments (*args):")
    for index, value in enumerate(args):
        print(f"  Argument {index}: {value}")
    print("Keyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

display_all(1, 2, 3, 4, name="Bob", age=25)  # Mixing regular, *args, and **kwargs


"""Unpacking Arguments: You can use * and ** to unpack iterables and dictionaries when calling functions."""

def sum_numbers(a, b, c):
    """Return the sum of three numbers."""
    return a + b + c

numbers = [1, 2, 3]
result = sum_numbers(*numbers)  # Unpacking list into positional arguments
print(f"Sum of numbers: {result}")

def display_person_info(name, age, city):
    """Display information about a person."""
    print(f"{name} is {age} years old and lives in {city}.")

person_info = {'name': 'Charlie', 'age': 28, 'city': 'Los Angeles'}
display_person_info(**person_info)  # Unpacking dictionary into keyword arguments