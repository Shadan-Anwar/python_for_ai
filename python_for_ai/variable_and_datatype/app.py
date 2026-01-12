"""
Topic: Variables and Data Types
Description:
    This program demonstrates the use of variables and
    commonly used built-in data types in Python.

    Variables in Python are used to store data values in memory.
    Python is a dynamically typed language, meaning the data type of a variable is determined at runtime based on the value assigned to it.
    Common built-in data types include integers, floating-point numbers, strings, and booleans.

Author: Shadan Anwar
"""

# Integer data type
number: int = 5
print("Number:", number)
print("Data type:", type(number))

print("-" * 30)

# Floating-point data type
float_number: float = 5.2
print("Float Number:", float_number)
print("Data type:", type(float_number))

print("-" * 30)

# String data type
name: str = "John Doe"
print("Name:", name)
print("Data type:", type(name))

print("-" * 30)

# Boolean data type (True)
is_active: bool = True
print("Flag value:", is_active)
print("Data type:", type(is_active))

print("-" * 30)

# Boolean data type (False)
is_disabled: bool = False
print("Flag value:", is_disabled)
print("Data type:", type(is_disabled))
