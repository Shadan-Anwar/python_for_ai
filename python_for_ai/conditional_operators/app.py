"""
File Name: app.py
Author: Shadan Anwar
Description:
This file explains conditional statements in Python using
if, elif, and else along with logical operators such as
AND and OR.

Conditional logic is a foundation of:
- Decision making systems
- AI & ML rule engines
- Agentic AI behavior selection
"""

# ---------------------------------------------------------
# BASIC VARIABLES
# ---------------------------------------------------------

age = 19
indian = False
student = True


# ---------------------------------------------------------
# EXAMPLE 1: SIMPLE if-elif-else CONDITION
# ---------------------------------------------------------

if age >= 18:
    print("You can vote.")
elif age <= 5:
    print("You are a child.")
else:
    print("You cannot vote.")


# ---------------------------------------------------------
# EXAMPLE 2: USING AND / OR WITH CONDITIONS
# ---------------------------------------------------------

if age >= 18 and indian:
    print("You are eligible to vote in India.")
elif age <= 17 or student:
    print("You are a student.")
else:
    print("You are not eligible to vote.")


# =========================================================
# 5 EXAMPLES USING AND OPERATOR
# =========================================================
# AND operator returns True only if ALL conditions are True

# Example 1
age = 25
indian = True
if age >= 18 and indian:
    print("Example 1: Eligible voter")

# Example 2
marks = 85
attendance = 90
if marks >= 60 and attendance >= 75:
    print("Example 2: Passed exam")

# Example 3
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Example 3: Login successful")

# Example 4
temperature = 30
humidity = 60
if temperature > 25 and humidity > 50:
    print("Example 4: Hot and humid weather")

# Example 5
battery = 80
charging = False
if battery > 50 and not charging:
    print("Example 5: Battery is sufficient")


# =========================================================
# 5 EXAMPLES USING OR OPERATOR
# =========================================================
# OR operator returns True if ANY ONE condition is True

# Example 1
age = 16
student = True
if age < 18 or student:
    print("Example 1: Student concession applicable")

# Example 2
is_admin = False
is_manager = True
if is_admin or is_manager:
    print("Example 2: Access granted")

# Example 3
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Example 3: Weekend")

# Example 4
internet = False
mobile_data = True
if internet or mobile_data:
    print("Example 4: Internet available")

# Example 5
error = False
warning = True
if error or warning:
    print("Example 5: System notification triggered")


# =========================================================
# WHY CONDITIONS ARE IMPORTANT FOR AI & AGENTIC AI
# =========================================================
# - Decision making
# - Rule-based agents
# - Behavior selection
# - Environment responses
# - Autonomous control flows
#
# Agentic AI systems heavily rely on conditional logic
# to decide actions based on environment state.
