"""
===========================================================
PYTHON DECORATORS — COMPLETE MASTER FILE
===========================================================

This file explains Python decorators from absolute basics
to advanced real-world usage.

Each section contains:
- Explanation (in comments)
- Decorator implementation
- 5 working examples

Author: Shadan Anwar
Purpose: Learning + Interview Preparation
"""

import time
from functools import wraps


# ===========================================================
# SECTION 1: FUNCTION AS FIRST-CLASS OBJECTS (FOUNDATION)
# ===========================================================
# In Python, functions can:
# - Be assigned to variables
# - Be passed as arguments
# - Be returned from other functions
# Decorators are built on this concept.


def greet():
    return "Hello"


def call_function(func):
    """Accepts a function and executes it"""
    return func()


print(call_function(greet))


# ===========================================================
# SECTION 2: SIMPLE DECORATOR (NO ARGUMENT FUNCTION)
# ===========================================================
# A decorator is a function that:
# - Takes another function as input
# - Returns a modified function


def simple_logger(func):
    """
    Logs the function name before execution
    """
    @wraps(func)
    def wrapper():
        print(f"[LOG] Function '{func.__name__}' is called")
        return func()
    return wrapper


# ---------- Examples (5) ----------

@simple_logger
def ex1():
    print("Example 1")


@simple_logger
def ex2():
    print("Example 2")


@simple_logger
def ex3():
    print("Example 3")


@simple_logger
def ex4():
    print("Example 4")


@simple_logger
def ex5():
    print("Example 5")


ex1()
ex2()
ex3()
ex4()
ex5()


# ===========================================================
# SECTION 3: BEFORE & AFTER EXECUTION DECORATOR
# ===========================================================
# Adds behavior before and after function execution


def before_after(func):
    @wraps(func)
    def wrapper():
        print(">> Before execution")
        result = func()
        print("<< After execution")
        return result
    return wrapper


# ---------- Examples (5) ----------

@before_after
def task1():
    print("Task 1 running")


@before_after
def task2():
    print("Task 2 running")


@before_after
def task3():
    print("Task 3 running")


@before_after
def task4():
    print("Task 4 running")


@before_after
def task5():
    print("Task 5 running")


task1()
task2()
task3()
task4()
task5()


# ===========================================================
# SECTION 4: MODIFY RETURN VALUE DECORATOR
# ===========================================================
# This decorator modifies the output of a function


def to_upper(func):
    """
    Converts function return value to uppercase
    """
    @wraps(func)
    def wrapper():
        return func().upper()
    return wrapper


# ---------- Examples (5) ----------

@to_upper
def greet1():
    return "hello"


@to_upper
def greet2():
    return "python"


@to_upper
def greet3():
    return "decorators"


@to_upper
def greet4():
    return "are powerful"


@to_upper
def greet5():
    return "learning"


print(greet1())
print(greet2())
print(greet3())
print(greet4())
print(greet5())


# ===========================================================
# SECTION 5: UNIVERSAL DECORATOR (*args, **kwargs)
# ===========================================================
# Real-world decorators MUST support any number of arguments


def universal_logger(func):
    """
    Logs arguments and return value
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Args:", args)
        print("Kwargs:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return wrapper


# ---------- Examples (5) ----------

@universal_logger
def add(a, b):
    return a + b


@universal_logger
def multiply(a, b, c):
    return a * b * c


@universal_logger
def greet_user(name):
    return f"Hello {name}"


@universal_logger
def power(base, exp=2):
    return base ** exp


@universal_logger
def info(name, age, city="NA"):
    return f"{name} - {age} - {city}"


add(2, 3)
multiply(2, 3, 4)
greet_user("Shadan")
power(5)
info("Shadan", 28, city="Delhi")


# ===========================================================
# SECTION 6: EXECUTION TIME DECORATOR
# ===========================================================
# Used for performance monitoring


def timer(func):
    """
    Measures execution time of a function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper


# ---------- Examples (5) ----------

@timer
def slow1():
    time.sleep(0.5)


@timer
def slow2():
    time.sleep(0.2)


@timer
def slow3():
    time.sleep(0.1)


@timer
def slow4():
    time.sleep(0.3)


@timer
def slow5():
    time.sleep(0.4)


slow1()
slow2()
slow3()
slow4()
slow5()


# ===========================================================
# SECTION 7: INPUT VALIDATION DECORATOR
# ===========================================================
# Prevents function execution if validation fails


def positive_numbers_only(func):
    """
    Allows execution only if all positional arguments are positive
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        for num in args:
            if num <= 0:
                print("[ERROR] All numbers must be positive")
                return
        return func(*args, **kwargs)
    return wrapper


# ---------- Examples (5) ----------

@positive_numbers_only
def calc1(a, b):
    print(a + b)


@positive_numbers_only
def calc2(a, b, c):
    print(a * b * c)


@positive_numbers_only
def calc3(x):
    print(x * x)


@positive_numbers_only
def calc4(a, b):
    print(a - b)


@positive_numbers_only
def calc5(a, b):
    print(a / b)


calc1(2, 3)
calc2(1, 2, -3)   # blocked
calc3(5)
calc4(10, 2)
calc5(8, 4)


# ===========================================================
# SECTION 8: DECORATOR WITH ARGUMENTS (ADVANCED)
# ===========================================================
# A decorator that itself takes arguments


def repeat(n):
    """
    Repeats function execution n times
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"[Repeat {i+1}]")
                func(*args, **kwargs)
        return wrapper
    return decorator


# ---------- Examples (5) ----------

@repeat(2)
def r1():
    print("Run 1")


@repeat(3)
def r2():
    print("Run 2")


@repeat(1)
def r3():
    print("Run 3")


@repeat(4)
def r4():
    print("Run 4")


@repeat(5)
def r5():
    print("Run 5")


r1()
r2()
r3()
r4()
r5()


# ===========================================================
# FINAL NOTES
# ===========================================================
# - Decorators are heavily used in frameworks (Flask, Django, FastAPI)
# - Common real-world use cases:
#   logging, auth, caching, retries, validation, monitoring
# - Mastering decorators improves code reusability & readability
