"""
File Name: app.py
Author: Shadan Anwar
Description:
This file explains the concept of loops in Python with clear,
professional examples. Loops are used to execute repetitive tasks
and are a core concept for software development, AI, ML, and
Agentic AI systems.

Topics Covered:
- for loop
- while loop
- Dictionary iteration
- break and continue
- for-else loop
"""

# ---------------------------------------------------------
# WHAT IS A LOOP?
# ---------------------------------------------------------
# A loop is a control structure that allows us to repeat
# a block of code multiple times.
#
# Python supports:
# 1. for loop
# 2. while loop
# Control statements:
# - break
# - continue
# - else


# ---------------------------------------------------------
# EXAMPLE 1: FOR LOOP WITH A LIST
# ---------------------------------------------------------

numbers = [1, 5, 6, 8, 9, 2]

for number in numbers:
    print("Number:", number)


# ---------------------------------------------------------
# EXAMPLE 2: FOR LOOP WITH DICTIONARY (KEYS)
# ---------------------------------------------------------

person = {
    "name": "Shaddy",
    "age": 30,
    "complexion": "Fair",
    "course": "Python"
}

for key in person:
    print(f"{key} : {person[key]}")


# ---------------------------------------------------------
# EXAMPLE 3: USING ENUMERATE WITH DICTIONARY
# ---------------------------------------------------------

for index, key in enumerate(person):
    print(f"Index {index} -> {key}")


# ---------------------------------------------------------
# EXAMPLE 4: DICTIONARY USING .items()
# ---------------------------------------------------------

for key, value in person.items():
    print(f"{key} = {value}")


# ---------------------------------------------------------
# EXAMPLE 5: WHILE LOOP WITH INPUT VALIDATION
# ---------------------------------------------------------

def is_invalid_age():
    """
    This function checks whether the user input
    is a valid numeric value or not.
    """
    user_input = input("Enter your age: ")
    print("Input type:", type(user_input))

    if not user_input.isdigit():
        return True
    return False


while is_invalid_age():
    print("Invalid input! Please enter digits only.")

print("Valid age entered.")


# ---------------------------------------------------------
# EXAMPLE 6: FOR LOOP WITH range()
# ---------------------------------------------------------

for i in range(1, 6):
    print("Value:", i)


# ---------------------------------------------------------
# EXAMPLE 7: BREAK STATEMENT
# ---------------------------------------------------------

numbers = [2, 4, 6, 8, 10]

for num in numbers:
    if num == 6:
        print("Number found. Exiting loop.")
        break
    print("Current number:", num)


# ---------------------------------------------------------
# EXAMPLE 8: CONTINUE STATEMENT
# ---------------------------------------------------------

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print("Odd number:", i)


# ---------------------------------------------------------
# EXAMPLE 9: FOR-ELSE LOOP
# ---------------------------------------------------------

search_numbers = [1, 3, 5]

for num in search_numbers:
    if num == 2:
        print("Number found")
        break
else:
    print("Number not found in the list")


# ---------------------------------------------------------
# EXAMPLE 10: NESTED LOOP
# ---------------------------------------------------------

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")


# ---------------------------------------------------------
# WHY LOOPS ARE IMPORTANT FOR AI & AGENTIC AI
# ---------------------------------------------------------
# - Iterating over datasets
# - Training machine learning models
# - Multi-agent coordination
# - Decision-making cycles
# - Reinforcement learning steps
#
# Loops are fundamental to building autonomous
# and intelligent AI systems.
