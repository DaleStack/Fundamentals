"""Scope refers to the visibility and lifetime of variables within different parts of a program."""
"""There is LEGB rule in Python which defines the order in which scopes are searched for variable names:
L: Local — Names defined within a function.
E: Enclosing — Names defined in the local scope of any and all enclosing functions.
G: Global — Names defined at the top level of a module or declared global using the global keyword.
B: Built-in — Names preassigned in the built-in names module."""


# Example of Local Scope

def local_scope_example():
    """This function demonstrates local scope."""
    local_var = "I am local"
    print(local_var)  # Accessible here

# Function inside a function to demonstrate Enclosing Scope

def enclosing_scope_example():
    """This function demonstrates enclosing scope."""
    enclosing_var = "I am enclosing"

    def inner_function():
        print(enclosing_var)  # Accessible here

    inner_function()

# Example of Global Scope

global_var = "I am global"  # Global variable

def global_scope_example():
    """This function demonstrates global scope."""
    print(global_var)  # Accessible here

global_scope_example()

print(global_var)  # Accessible here


# Naming Variables

x = "global x"  # Global variable

def variable_naming_example():
    x = "local x"  # Local variable
    print(x)  # Prints local x

variable_naming_example()
print(x)  # Prints global x


"""Global Keyword: The global keyword is used to declare that a variable inside a function is global."""

def modify_global():
    global global_var
    global_var = "Modified global variable"

modify_global()
print(global_var)  # Prints modified global variable

# To change a global variable inside a function, you must use the global keyword.

y = 10  # Global variable

def change_global_y():
    global y
    y = 20  # Modify the global variable

change_global_y()
print(y)  # Prints modified global variable


# Nonlocal Keyword: The nonlocal keyword is used to declare that a variable inside a nested 
# function is not local to that function.

def outer_function():
    outer_var = "I am outer"

    def inner_function():
        nonlocal outer_var # Declare that we want to use the outer function's variable
        outer_var = "Modified outer variable"
    
    inner_function()
    print(outer_var)  # Prints modified outer variable

outer_function()
