"""The input() function in Python is used to take input from the user via the console. It reads a line from input,
returns it as a string, and can optionally display a prompt to the user."""

# This script takes a name as input from the user and greets them.
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Taking multiple inputs and converting them to integers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(type(num1), type(num2))


