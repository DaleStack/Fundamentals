"""Python comprehensions provide a concise way to create lists, sets, or dictionaries."""


# Example 1: List comprehension

squares = [x**2 for x in range(10)] # A list is created with brackets []
print(squares)

# Normal way 
squares_normal = list()
for x in range(10):
    squares_normal.append(x**2)
print(squares_normal)

# List comprehension with condition

even_squares = [x for x in range(10) if x % 2 == 0]
print(even_squares)

# Example 2: Set comprehension

unique_squares = {x**2 for x in range(10)} # A set is created with curly braces {}
print(unique_squares)

# Normal way 
unique_squares_normal = set()
for x in range(10):
    unique_squares_normal.add(x**2)
print(unique_squares_normal)

# Example 3: Dictionary comprehension

square_dict = {x: x**2 for x in range(10)} # A dictionary is created with curly braces {}
print(square_dict)

# Normal way
square_dict_normal = dict()
for x in range(10):
    square_dict_normal[x] = x**2

print(square_dict_normal)

# Example 4: Nested comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)

# Normal way
matrix_normal = list()
for i in range(1, 4):
    matrix_row = list()
    for j in range(1, 4):
        matrix_row.append(i * j)
    matrix_normal.append(matrix_row)

print(matrix_normal)

# Example 5: Comprehension with function

def plus_one(x):
    return x + 1

plus_one_list = [plus_one(x) for x in range(5)]

print(plus_one_list)

    