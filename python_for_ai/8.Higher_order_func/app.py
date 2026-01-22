"""
File Name: app.py
Author: Shadan Anwar
Topic: Higher Order Functions in Python

Description:
This file demonstrates Higher Order Functions (HOFs) in Python.
A Higher Order Function is a function that:
1. Accepts another function as an argument, OR
2. Returns a function as output

Covered concepts:
- Function as argument
- map()
- filter()
- reduce()
- zip()
- enumerate()
"""

from functools import reduce


# -------------------------------------------------
# Example 1: Function as an argument (Addition)
# -------------------------------------------------

def add(x, y):
    """Returns sum of two numbers"""
    return x + y


def calculate(func, a, b):
    """
    Accepts a function as argument
    Calls that function with given values
    """
    return func(a, b)


result = calculate(add, 5, 2)
print("Result (Addition using HOF):", result)


# -------------------------------------------------
# Example 2: Function as an argument (Multiplication)
# -------------------------------------------------

def product(a, b):
    """Returns product of two numbers"""
    return a * b


def multiply(func, x, y):
    """
    Accepts multiplication function
    and executes it
    """
    return func(x, y)


output = multiply(product, 5, 5)
print("Output (Multiplication using HOF):", output)


# -------------------------------------------------
# Example 3: map() – Transform elements
# -------------------------------------------------

# map() applies a function to each element
numbers = [1, 2, 3, 4, 5]

map_result = list(map(lambda x: x * 2, numbers))
print("Result using map():", map_result)


# -------------------------------------------------
# Example 4: filter() – Select elements
# -------------------------------------------------

# filter() keeps elements based on condition
filter_result = list(filter(lambda x: x % 2 == 0, numbers))
print("Result using filter() (Even numbers):", filter_result)


# -------------------------------------------------
# Example 5: reduce() – Combine elements into one
# -------------------------------------------------

# reduce() reduces a list into a single value
reduce_result = reduce(lambda x, y: x + y, numbers)
print("Result using reduce() (Sum):", reduce_result)


# -------------------------------------------------
# Example 6: zip() – Combine multiple iterables
# -------------------------------------------------

names = ["Shaddy", "Ayra", "Kamyar", "Aashi"]

zip_result = list(zip(numbers, names))
print("Result using zip():", zip_result)


# -------------------------------------------------
# Example 7: enumerate() – Index with value
# -------------------------------------------------

# enumerate() provides index and value together
print("Result using enumerate():")
for index, value in enumerate(numbers):
    print(index, value)


# -------------------------------------------------
# End of file
# -------------------------------------------------
