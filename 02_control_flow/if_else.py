"""Python if-else statement compares values and executes code based on the result."""

# Example 1: Basic if-else statement

age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example 2: if-elif-else statement

age = 65
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Example 3: Nested if-else statement

score = 85
section = "A"

if section == "A":
    if score >= 90:
        print("Excellent in section A.")
    elif score >= 75:
        print("Good in section A.")
    else:
        print("Needs improvement in section A.")
else:
    print("You are not in section A.")


# Example 4: Short hand if-else (Ternary operator)

num = 10
print("Even") if num % 2 == 0 else print("Odd")

# Example 5: Logical operators with if-else
# AND OR NOT

temperature = 25
humidity = 60

if temperature > 20 and humidity < 70:
    print("The weather is pleasant.")
elif temperature > 30 or humidity > 80:
    print("The weather is uncomfortable.")
elif not (temperature < 10):
    print("The weather is moderate.")
else:
    print("The weather is cold.")

# Example 6: Using if-else in a function

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
result = check_even_odd(7)
print(f"The number is {result}.")

# Example 7: Pass Statement in if-else

value = 42

if value > 50:
    pass # Placeholder for future code or when a statement is required syntactically but no action is needed
else:
    print("Value is 50 or less.")
    
