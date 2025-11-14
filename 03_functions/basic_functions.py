"""A function is a reusable block of code that performs a specific task."""


# Example of a basic function
"""A function is defined using the 'def' keyword, followed by the function name and parentheses."""

def say_hello():
    """This function prints a greeting message."""
    print("Hello!")

# Calling the function

say_hello()

"""Why use functions?
1. Reusability: Functions allow you to reuse code without rewriting it.
2. Organization: Functions help organize code into manageable sections.
3. Readability: Functions can make code easier to read and understand.
4. Maintainability: Functions make it easier to update and maintain code.
5. Abstraction: Functions allow you to hide complex logic behind a simple interface.
6. Testing: Functions can be tested independently, making debugging easier.
7. Modularity: Functions promote modular programming, allowing for better collaboration and code management.
8. Efficiency: Functions can improve code efficiency by reducing redundancy.
9. Scope Management: Functions create their own scope, helping to avoid variable name conflicts.
10. Parameterization: Functions can accept parameters, allowing for dynamic behavior based on input."""

# Without functions, converting miles to kilometers would require repetitive code

miles_1 = 10
kilometers_1 = miles_1 * 1.60934
print(f"miles: {miles_1}, kilometers: {kilometers_1}")

miles_2 = 25
kilometers_2 = miles_2 * 1.60934
print(f"miles: {miles_2}, kilometers: {kilometers_2}")

miles_3 = 50
kilometers_3 = miles_3 * 1.60934
print(f"miles: {miles_3}, kilometers: {kilometers_3}")

# With functions, we can encapsulate the conversion logic
def miles_to_kilometers(miles):
    """Convert miles to kilometers."""
    return miles * 1.60934

# Now we can reuse the function for different values
miles_list = [10, 25, 50]
for miles in miles_list:
    kilometers = miles_to_kilometers(miles)
    print(f"miles: {miles}, kilometers: {kilometers}")

"""Return Statement: A return statement is used to exit a function and return a value to the caller."""

def add(a, b):
    return a + b

result = add(5, 3)
print(f"The sum is: {result}")


"""Pass Statement: The pass statement is a placeholder that does nothing. It is used when a statement is syntactically 
required but no action is needed."""
def placeholder_function():
    pass  # This function does nothing for now


