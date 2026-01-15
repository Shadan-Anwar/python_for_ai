"""
File Name: app.py
Author: Shadan Anwar
Description:
This file explains Python functions in a clear and professional way.
Functions allow us to write reusable, organized, and maintainable code.
They are heavily used in software development, AI, ML, and Agentic AI
systems for modular logic and decision-making.

Topics Covered:
- What is a function
- Function naming rules
- Functions without parameters
- Functions with parameters
- Return values
"""

# ---------------------------------------------------------
# WHAT IS A FUNCTION?
# ---------------------------------------------------------
# A function is a reusable block of code designed
# to perform a specific task.
#
# Benefits:
# - Code reusability
# - Better readability
# - Easier maintenance
# - Modular design (important for AI systems)


# ---------------------------------------------------------
# FUNCTION NAMING RULES
# ---------------------------------------------------------
# 1. Function name must start with a letter or underscore (_)
# 2. It can contain letters, numbers, and underscores
# 3. Function names are case-sensitive
# 4. Use lowercase_with_underscores (recommended style)


# ---------------------------------------------------------
# EXAMPLE 1: FUNCTION WITHOUT PARAMETERS
# ---------------------------------------------------------

def hello_function():
    """Prints a greeting message."""
    print("Hello all of you!")


hello_function()


# ---------------------------------------------------------
# EXAMPLE 2: FUNCTION WITH PARAMETER
# ---------------------------------------------------------

def calculate_age(year_of_birth):
    """
    Calculates age based on year of birth.
    """
    current_year = 2026
    return current_year - year_of_birth


age = calculate_age(1997)
print("Your age in years:", age)


# ---------------------------------------------------------
# EXAMPLE 3: FUNCTION WITH MULTIPLE PARAMETERS
# ---------------------------------------------------------

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


result = add_numbers(10, 20)
print("Sum:", result)


# ---------------------------------------------------------
# EXAMPLE 4: FUNCTION WITH DEFAULT PARAMETER
# ---------------------------------------------------------

def greet_user(name="Guest"):
    """Greets user with a default name."""
    print(f"Hello, {name}!")


greet_user()
greet_user("Shadan")


# ---------------------------------------------------------
# EXAMPLE 5: FUNCTION RETURNING BOOLEAN VALUE
# ---------------------------------------------------------

def is_adult(age):
    """Checks whether a person is an adult."""
    return age >= 18


print("Is adult:", is_adult(19))


# ---------------------------------------------------------
# EXAMPLE 6: FUNCTION WITH CONDITIONAL LOGIC
# ---------------------------------------------------------

def check_voting_eligibility(age, is_indian):
    """Determines voting eligibility."""
    if age >= 18 and is_indian:
        return "Eligible to vote"
    return "Not eligible to vote"


print(check_voting_eligibility(20, True))


# ---------------------------------------------------------
# EXAMPLE 7: FUNCTION WORKING WITH LIST
# ---------------------------------------------------------

def calculate_average(numbers):
    """Returns average of a list of numbers."""
    return sum(numbers) / len(numbers)


marks = [70, 80, 90]
print("Average marks:", calculate_average(marks))


# ---------------------------------------------------------
# WHY FUNCTIONS ARE IMPORTANT FOR AI & AGENTIC AI
# ---------------------------------------------------------
# - Modular decision-making
# - Reusable agent behaviors
# - Clean pipeline design
# - Easier debugging
# - Scalable AI architectures
#
# In Agentic AI, each agent behavior
# is often implemented as a function.
