"""Python loops are used for iterating over sequences like lists, tuples, or strings."""

"""While Loop is used to execute a block of code as long as a condition is true."""

# Example 1: While loop 
count = 0 

while count < 5:
    print(f"count is {count}")
    count += 1

"""Infinite while loops run indefinitely until externally stopped. Be cautious when using them. This can cause stack 
overflow or unresponsive programs."""
# Uncomment the following line to see an infinite loop in action

# while True:
#     print("This will run forever unless interrupted.")


# Example 2: While loop with break and continue
num = 0

while num < 10:
    num += 1
    if num % 2 == 0:
        continue # Skip even numbers
    if num > 7:
        break # Exit loop if num is greater than 7
    print(f"Odd number: {num}")

# Example 3: While loop with else
n = 0

while n < 3:
    print(f"This is iteration {n}")
    n += 1
else:
    print("While loop has completed normally.")



"""For Loop is for iterating over a sequence (like a list, tuple, dictionary, set, or string)."""
# Example 3: For loop 
fruits = ["Apple", "Orange", "Banana"]

for fruit in fruits:
    print(f"I like {fruit}")

# Example 4: For loop with break

names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    if name == "Charlie":
        print("Breaking the loop at Charlie")
        break
    print(name)

# Example 5: For loop with continue

nums = [1, 2, 3, 4, 5, 6]

for num in nums:
    if num == 3:
        print("Skipping number 3")
        continue
    print(f"Number: {num}")

# Example 6: For loop with range() function

for i in range(5):
    print(f"Iteration {i}")

for i in range(2, 10): # Start from 2 and end before 10 so this will print 2 to 9
    print(f"Number from 2 to 9: {i}")

for i in range(1, 11, 1): # Start from 1 to 10 with a step of 1
    print(f"Odd number between 1 and 10: {i}")


# Example 7: For loop with else

for letter in "Python":
    print(f"Current letter: {letter}")
else:
    print("For loop has completed normally.")


