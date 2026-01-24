"""
===========================================================
📌 PYTHON EXCEPTION HANDLING - COMPLETE BEGINNER GUIDE
Author: Shadan Anwar
Purpose: Learn how to handle errors gracefully in Python
===========================================================

👉 Exception Handling prevents program crashes
👉 It helps handle runtime errors safely
"""

# =========================================================
# 1️⃣ WHAT IS EXCEPTION HANDLING (THEORY)
# =========================================================

# Exception handling is a process of handling runtime errors
# so that the program does not crash unexpectedly.

# TYPES OF ERRORS:
# 1. Syntax Error   -> Code is grammatically wrong (won't run)
# 2. Logical Error  -> Code runs but gives wrong output
# 3. Runtime Error  -> Error occurs while program is running


# =========================================================
# 2️⃣ GENERIC TRY - EXCEPT EXAMPLES
# =========================================================

# -------- Example 1: Division Error --------
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except Exception as e:
    print("Error occurred:", e)


# -------- Example 2: Invalid Input --------
try:
    num = int(input("Enter a number: "))
    print("Square:", num * num)
except Exception as e:
    print("Invalid input:", e)


# =========================================================
# 3️⃣ TRY - EXCEPT - FINALLY (RESOURCE HANDLING)
# =========================================================

# -------- Example 1: File Reading --------
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("File closed safely")


# -------- Example 2: Database Simulation --------
try:
    print("Connecting to database...")
    raise Exception("Database connection failed")
except Exception as e:
    print("Error:", e)
finally:
    print("Database connection closed")


# =========================================================
# 4️⃣ SAFE LIST INDEXING (IndexError)
# =========================================================

numbers = [10, 20, 30, 40, 50]

# -------- Example 1 --------
try:
    index = int(input("Enter index: "))
    print(numbers[index])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Index must be an integer")


# -------- Example 2 --------
try:
    print(numbers[10])
except IndexError:
    print("Invalid index accessed")


# =========================================================
# 5️⃣ STRING TO INTEGER CONVERSION (ValueError)
# =========================================================

# -------- Example 1 --------
user_input = input("Enter a number string: ")
try:
    print(int(user_input))
except ValueError:
    print("Conversion failed")


# -------- Example 2 --------
try:
    age = int("twenty")
except ValueError:
    print("Age must be numeric")


# =========================================================
# 6️⃣ FILE HANDLING WITH PROPER EXCEPTION
# =========================================================

# -------- Example 1 --------
try:
    with open("sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("sample.txt not found")


# -------- Example 2 --------
try:
    with open("notes.txt", "w") as file:
        file.write("Learning Python Exception Handling")
except Exception as e:
    print("Write failed:", e)


# =========================================================
# 7️⃣ CUSTOM EXCEPTIONS USING RAISE
# =========================================================

# -------- Example 1: Bank Withdrawal --------
def withdraw(amount, balance):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    elif amount > balance:
        raise ValueError("Insufficient balance")
    else:
        print("Remaining balance:", balance - amount)


try:
    withdraw(5000, 2000)
except ValueError as e:
    print("Transaction failed:", e)


# -------- Example 2: Age Validation --------
def check_age(age):
    if age < 0 or age > 120:
        raise ValueError("Invalid age")
    print("Valid age")


try:
    check_age(150)
except ValueError as e:
    print("Error:", e)


# =========================================================
# 8️⃣ MULTIPLE EXCEPT BLOCKS
# =========================================================

# -------- Example 1 --------
try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print(x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter numbers only")


# -------- Example 2 --------
try:
    data = [1, 2, 3]
    print(data[5])
except IndexError:
    print("Index error occurred")
except Exception as e:
    print("Unknown error:", e)


# =========================================================
# 9️⃣ FINAL NOTES
# =========================================================

"""
✔ Always use specific exceptions when possible
✔ Use 'with open()' for file handling
✔ Use finally for cleanup
✔ Use raise to create custom errors

Happy Coding 🚀
"""
