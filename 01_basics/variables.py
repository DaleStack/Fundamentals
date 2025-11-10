"""Python variables are used to store data values. A variable is created the moment you first assign a value 
to it. Variables do not need explicit declaration to reserve memory space."""

# Creating variables
x = 5
x = "Alice"

# or single quote
x = 'Alice'

# Case Sensitivity
"""These are three different variables due to case sensitivity."""
age = 25
Age = 30
aGe = 35

"""Variable names must start with a letter or the underscore character. They cannot start with a number.
Variable names should not be the same as Python keywords."""

# Common variable naming conventions

# 1. Camel Case
myVariableName = "Edward" # This is called Camel Case because of the capital letters in the middle of the name.

# 2. Pascal Case 
MyVariableName = "Edward" # This is called Pascal Case because of the capital letters at the beggining of each word.

# 3. Snake Case
my_variable_name = "Edward" # This is called Snake Case because of the underscores between each word.


"""Multiple variables can be assigned in one line."""

x, y, z = "Orange", "Apple", "Banana"

print("######################################")
print("#                                    #")
print("# Many Values to Multiple Variables: #")
print("#                                    #")
print("######################################")
print(x)
print(y)
print(z)

"""One value can be assigned to multiple variables."""

x = y = z = "Orange"

print("##############################")
print("#                            #")
print("# One to Multiple Variables: #")
print("#                            #")
print("##############################")
print(x)
print(y)
print(z)


"""Unpack a collection into variables."""

fruits = ["Apple", "Orange", "Banana"]
x, y, z = fruits
print("######################################")
print("#                                    #")
print("# Unpacking collection in variables: #")
print("#                                    #")
print("######################################")
print(x)
print(y)
print(z)


"""Output variables."""

x = "I"
y = "am"
z = "Dale"

print("#################################################")
print("#                                               #")
print("# Output multiple variables separated by comma: #")
print("#                                               #")
print("#################################################")
print(x, y, z)

x = "I "
y = "am "
z = "Dale"

print("##############################################")
print("#                                            #")
print("# Output multiple variables separated by + : #")
print("#                                            #")
print("##############################################")
print(x + y + z)



"""For numbers, the + operator works as a mathematical operator."""

x = 5
y = 10

print("#####################")
print("#                   #")
print("# Numbers Example : #")
print("#                   #")
print("#####################")
print(x + y)

"""print() function gives you error if you try to combine strings and numbers"""

x = 5
y = "Hello"
# print(x + y) will give you an error, use comma instead

print("##########################################")
print("#                                        #")
print("# Combining String and Numbers Example : #")
print("#                                        #")
print("##########################################")
print(x, y)


"""Global variables can be accessed inside functions."""

my_name = "Dale"

def print_name():
    print(f"My name is {my_name}")

print("############################")
print("#                          #")
print("# Using Global Variables : #")
print("#                          #")
print("############################")

print_name()

"""This example will create a local variable with the same name as the global variable."""

def change_name():
    my_name = "Alice"
    print(f"My name inside function is {my_name}")

change_name()

print(f"My name outside function is {my_name}")


"""To create a global variable inside a function, use the global keyword."""

print("##########################")
print("#                        #")
print("# Using Global Keyword : #")
print("#                        #")
print("##########################")

def set_name():
    global my_name
    my_name = "Bob"

set_name()

print(f"My name after using global keyword is {my_name}")

"""To change the value of a global variable inside a function, use the global keyword."""

my_name_value = "Charlie"

def modify_name():
    global my_name_value
    my_name_value = "Eddie"

modify_name()

print(f"My name after modifying global variable is {my_name_value}")
