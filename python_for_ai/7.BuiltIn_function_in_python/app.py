"""
File Name: builtin_functions_in_python.py
Author: Shadan Anwar
Description:
This file explains built-in functions in Python with clear
definitions and practical examples.

Built-in functions are predefined functions provided by Python.
They are always available and do not require any external
library or import.

Built-in functions are heavily used in:
- Data processing
- AI & ML pipelines
- Agentic AI decision systems
"""

# ---------------------------------------------------------
# WHAT IS A BUILT-IN FUNCTION?
# ---------------------------------------------------------
# A built-in function is a function that is already
# available in Python by default.
#
# These functions help us perform common tasks such as:
# - Printing output
# - Getting user input
# - Type conversion
# - Mathematical operations
# - Iteration and filtering


# ---------------------------------------------------------
# COMMON BUILT-IN FUNCTIONS WITH EXAMPLES
# ---------------------------------------------------------

# Example 1: print() → Displays output
print("Hello, Python Built-in Functions!")


# Example 2: type() → Returns the data type of a variable
value = 10
print("Data type:", type(value))


# Example 3: input() → Takes input from the user
# user_name = input("Enter your name: ")
# print("Hello,", user_name)


# Example 4: len() → Returns length of an object
numbers = [1, 2, 3, 4, 5]
print("Length of list:", len(numbers))


# Example 5: sum() → Returns sum of elements
print("Sum of numbers:", sum(numbers))


# ---------------------------------------------------------
# TYPE CONVERSION BUILT-IN FUNCTIONS
# ---------------------------------------------------------

# Example 6: int()
age = "25"
print("Converted to int:", int(age))

# Example 7: float()
price = "99.99"
print("Converted to float:", float(price))

# Example 8: str()
number = 100
print("Converted to string:", str(number))


# ---------------------------------------------------------
# ITERATION & LOGICAL BUILT-IN FUNCTIONS
# ---------------------------------------------------------

# Example 9: max() and min()
marks = [55, 78, 92, 66]
print("Maximum marks:", max(marks))
print("Minimum marks:", min(marks))


# Example 10: abs()
print("Absolute value:", abs(-45))


# ---------------------------------------------------------
# BOOLEAN & CHECKING FUNCTIONS
# ---------------------------------------------------------

# Example 11: isinstance()
print("Is integer:", isinstance(10, int))


# Example 12: all() → Returns True if all values are True
values = [True, True, True]
print("All values true:", all(values))


# Example 13: any() → Returns True if any value is True
values = [False, False, True]
print("Any value true:", any(values))


# ---------------------------------------------------------
# WHY BUILT-IN FUNCTIONS ARE IMPORTANT FOR AI & AGENTIC AI
# ---------------------------------------------------------
# - Fast data processing
# - Clean and readable code
# - Reduced external dependencies
# - Efficient decision checks
#
# Agentic AI systems heavily rely on built-in functions
# for perception, evaluation, and action selection.
