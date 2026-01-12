"""
Topic: Python Operators
Description:
    This program demonstrates the usage of different
    types of operators in Python with clear examples.

    Operators in Python are special symbols used to perform operations on variables and values.
    They are essential for mathematical calculations, comparisons, and decision-making logic, which form the foundation of AI, Machine Learning, and Agentic AI systems.

Author: Shadan Anwar
"""

# ==================================================
# ARITHMETIC OPERATORS
# ==================================================

# Addition
x: int = 2
y: int = 7
addition_result = x + y
print("Addition:", addition_result)

# Example 2
print("Addition Example 2:", 10 + 5)

# Example 3
print("Addition Example 3:", -3 + 8)

print("-" * 40)

# Subtraction
a: int = 7
b: int = 2
subtraction_result = a - b
print("Subtraction:", subtraction_result)

# Example 2
print("Subtraction Example 2:", 20 - 10)

# Example 3
print("Subtraction Example 3:", 5 - 12)

print("-" * 40)

# Multiplication
multiplication_result = a * b
print("Multiplication:", multiplication_result)

# Example 2
print("Multiplication Example 2:", 4 * 5)

# Example 3
print("Multiplication Example 3:", -3 * 6)

print("-" * 40)

# Division
division_result = a / b
print("Division:", division_result)

# Example 2
print("Division Example 2:", 10 / 2)

# Example 3
print("Division Example 3:", 7 / 3)

print("-" * 40)

# Floor Division
floor_division_result = a // b
print("Floor Division:", floor_division_result)

# Example 2
print("Floor Division Example 2:", 9 // 2)

# Example 3
print("Floor Division Example 3:", 20 // 3)

print("-" * 40)

# Modulus
modulus_result = a % b
print("Modulus:", modulus_result)

# Example 2
print("Modulus Example 2:", 10 % 3)

# Example 3
print("Modulus Example 3:", 15 % 4)

print("-" * 40)

# Exponential
exponential_result = a ** 2
print("Exponential:", exponential_result)

# Example 2
print("Exponential Example 2:", 2 ** 3)

# Example 3
print("Exponential Example 3:", 5 ** 0)

print("=" * 50)

# ==================================================
# COMPARISON OPERATORS
# ==================================================

x: int = 15
y: int = 10

print("x > y:", x > y)
print("x >= y:", x >= y)

# Example 2
print("10 > 20:", 10 > 20)

# Example 3
print("5 >= 5:", 5 >= 5)

print("-" * 40)

x = 5
y = 10
print("x < y:", x < y)
print("x <= y:", x <= y)

# Example 2
print("3 < 7:", 3 < 7)

# Example 3
print("8 <= 8:", 8 <= 8)

print("-" * 40)

x = 10
y = 10
print("x == y:", x == y)

# Example 2
print("5 == 6:", 5 == 6)

# Example 3
print("'AI' == 'AI':", "AI" == "AI")

print("=" * 50)

# ==================================================
# ASSIGNMENT OPERATOR
# ==================================================

num: int = 5
print("Assigned value:", num)

# Example 2
num += 3
print("After += 3:", num)

# Example 3
num *= 2
print("After *= 2:", num)

print("=" * 50)

# ==================================================
# LOGICAL OPERATORS
# ==================================================

x: bool = True
y: bool = False
z: bool = True

# AND Operator
print("AND (x and z):", x and z)

# Example 2
print("AND (x and y):", x and y)

# Example 3
print("AND (True and True):", True and True)

print("-" * 40)

# OR Operator
print("OR (x or y):", x or y)

# Example 2
print("OR (False or False):", False or False)

# Example 3
print("OR (True or False):", True or False)

print("-" * 40)

# NOT Operator (Correct Usage)
value: int = 5
condition_result = value > 10
print("Condition (value > 10):", condition_result)
print("NOT condition:", not condition_result)

# Example 2
print("NOT True:", not True)

# Example 3
print("NOT False:", not False)
