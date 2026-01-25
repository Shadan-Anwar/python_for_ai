"""
===========================================================
Object-Oriented Programming (OOP) in Python
Author: Shadan Anwar
Purpose: Beginner-friendly, professional OOP examples
===========================================================

This file covers:
1. What is a Class
2. What is an Object
3. Constructor (__init__)
4. Attributes & Methods
5. Multiple Objects
6. Real-world examples (House, Person, Car, Sensor, Bank)
7. Best Practices & Common Mistakes
"""

# =========================================================
# 1️⃣ WHAT IS A CLASS?
# ---------------------------------------------------------
# A class is a blueprint or template.
# It defines what data (attributes) and behavior (methods)
# an object will have.
# =========================================================


class House:
    """
    House class represents a real-world house.
    """

    def __init__(self, color, size):
        """
        Constructor:
        Automatically called when an object is created.

        self  -> current object
        color -> house color
        size  -> house size (e.g., 2BHK, 3BHK)
        """
        self.color = color
        self.size = size

    def get_details(self):
        """
        Method that returns house details.
        """
        return f"House color is {self.color} and size is {self.size}"


# =========================================================
# 2️⃣ WHAT IS AN OBJECT?
# ---------------------------------------------------------
# An object is a real instance created from a class.
# Each object has its own memory and data.
# =========================================================

my_house = House("Blue", "4BHK")
your_house = House("Green", "3BHK")

print(my_house.get_details())
print(your_house.get_details())


# =========================================================
# 3️⃣ PERSON CLASS (Attributes + Method)
# ---------------------------------------------------------
# Demonstrates:
# - Attributes (name, age)
# - Method (greet)
# - Multiple objects
# =========================================================


class Person:
    """
    Person class represents a human being.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """
        Prints a greeting message.
        """
        print(f"Hello, my name is {self.name}!")


# Creating multiple objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 40)

print(f"Name: {person1.name}, Age: {person1.age}")
person1.greet()

print(f"Name: {person2.name}, Age: {person2.age}")
person2.greet()

print(f"Name: {person3.name}, Age: {person3.age}")
person3.greet()


# =========================================================
# 4️⃣ CAR CLASS (Real-world Action)
# ---------------------------------------------------------
# Demonstrates:
# - Behavior using methods
# - Clean attribute naming
# =========================================================


class Car:
    """
    Car class represents a vehicle.
    """

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")


my_car = Car("Red", "Toyota")
your_car = Car("Black", "BMW")

my_car.drive()
your_car.drive()


# =========================================================
# 5️⃣ IoT-STYLE SENSOR CLASS
# ---------------------------------------------------------
# Demonstrates:
# - Practical IoT modeling
# - Data reading using methods
# =========================================================


class Sensor:
    """
    Sensor class represents an IoT sensor.
    """

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def read_value(self):
        return f"{self.name} reading is {self.value}"


temp_sensor = Sensor("Temperature Sensor", 36)
humidity_sensor = Sensor("Humidity Sensor", 60)

print(temp_sensor.read_value())
print(humidity_sensor.read_value())


# =========================================================
# 6️⃣ BANK ACCOUNT CLASS (Logic + Data)
# ---------------------------------------------------------
# Demonstrates:
# - Business logic
# - Condition handling inside methods
# =========================================================


class BankAccount:
    """
    BankAccount class represents a user's bank account.
    """

    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance")


account = BankAccount("Shaddy", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)


# =========================================================
# 7️⃣ COMMON BEGINNER MISTAKES (IMPORTANT)
# ---------------------------------------------------------
# ❌ print(object.method())  -> prints None if method returns nothing
# ✅ object.method()
#
# ❌ Using print instead of return when data is needed
# ✅ Use return for reusable values
# =========================================================


# =========================================================
# 8️⃣ INTERVIEW ONE-LINERS
# ---------------------------------------------------------
# Class       -> Blueprint for creating objects
# Object      -> Instance of a class
# Constructor -> Initializes object data
# Method      -> Function inside a class
# self        -> Refers to the current object
# =========================================================


print("\n--- OOP BASICS COMPLETED SUCCESSFULLY ---")
