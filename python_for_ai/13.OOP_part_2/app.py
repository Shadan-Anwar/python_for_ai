

# Python OOP Methods – Instance, Class & Static Methods

**Author: ** Shadan Anwar
**Level: ** Beginner → Interview Ready

---

# 📌 Description

This repository explains ** Instance Methods**, **Class Methods**, and **Static Methods ** in Python with **clear concepts, real-world examples, common mistakes, and interview explanations**.

All examples are written in **one single file style**, so beginners can read, run, and understand everything step by step.

---

# 📚 Table of Contents

1. What is OOP in Python?
2. Instance Method(with examples)
3. Class Method(with examples)
4. Static Method(with examples)
5. Mixed Practical Questions(Q1–Q9)
6. Comparison Table
7. Interview One‑Liners

---

# 1️⃣ What is OOP in Python?

Object-Oriented Programming(OOP) is a programming style where we group ** data(variables) ** and **behavior(methods) ** inside a class .

A class can contain ** three types of methods**:

* Instance Method
* Class Method
* Static Method

---

# 2️⃣ Instance Method

# 🔹 Definition

An ** instance method ** works with **object-level data**.

* First parameter is always `self`
* `self` represents the ** current object**

---

# Example 1: House Class

```python


class House:
    def __init__(self, color):
        self.color = color

    def details(self):
        print(f"Color of house is {self.color}")


my_house = House("Blue")
my_house.details()

white_house = House("White")
white_house.details()
```

# 🧠 Explanation

* `color` is an ** instance variable**
* Each object has its own data
* Instance methods access data using `self`

---

# Example 2: Circle Area

```python


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of the circle is {3.14 * self.radius * self.radius}")


circle = Circle(6)
circle.area()
```

📌 Use instance methods when ** logic depends on object data**.

---

# 3️⃣ Class Method

# 🔹 Definition

A ** class method ** works with **class -level data**.

* Uses `@ classmethod`
* First parameter is `cls`
* `cls` represents the ** class itself**

---

# Example 1: Access Class Variable

```python


class Employee:
    company = "Infosys"

    @classmethod
    def get_company(cls):
        return cls.company


print(Employee.get_company())
```

# 🧠 Explanation

* `company` is shared by all objects
* No object creation required

---

# Example 2: Alternative Constructor (Very Important)

```python


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split("-")
        return cls(name, int(salary))


emp = Employee.from_string("Rohit-5000")
print(emp.name)
print(emp.salary)
```

# 🧠 Deep Explanation

* `from_string()` creates and returns an object
* `cls()` internally calls `__init__`
* This is called an ** alternative constructor**

---

# Example 3: Class Configuration

```python


class AppConfig:
    environment = "DEV"

    @classmethod
    def set_env(cls, env):
        cls.environment = env

    def show_env(self):
        print("Environment:", self.environment)


print(AppConfig.environment)
AppConfig.set_env("DEVELOPMENT")

app = AppConfig()
app.show_env()
```

📌 Class methods are used to ** modify shared configuration**.

---

# 4️⃣ Static Method

# 🔹 Definition

A ** static method ** is a ** utility/helper function ** inside a class .

* Uses `@ staticmethod`
* No `self`
* No `cls`

---

# Example 1: Calculator Utility

```python


class Cal:
    @staticmethod
    def add(x, y):
        print(f"Addition result: {x + y}")


Cal.add(15, 3)
```

---

# Example 2: Validation Logic

```python


class UserValidator:
    @staticmethod
    def is_valid_age(age):
        return age >= 18


print(UserValidator.is_valid_age(19))
```

---

# Example 3: Static Method inside Instance Method

```python


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
        else:
            print("Invalid deposit amount")


acc = BankAccount("Shaddy", 100)
acc.deposit(1000)
print("Balance:", acc.balance)
```

🧠 Static methods are best for **validation and helper logic**.

---

# 5️⃣ Comparison Table

| Feature | Instance Method | Class Method | Static Method |
| -------------------- | --------------- | ------------ | ------------- |
| First argument | self | cls | None |
| Access instance data | ✅ | ❌ | ❌ |
| Access class data | ✅ | ✅ | ❌ |
| Create object | ❌ | ✅ | ❌ |
| Utility logic | ❌ | ❌ | ✅ |

---

# 6️⃣ Interview One‑Line Answers

* **Instance method: ** Works with object data using `self`
* **Class method: ** Works with class data using `cls`
* **Static method: ** Utility function related to the class

---

# ✅ Conclusion

Use:

* **Instance methods ** → object behavior
* **Class methods ** → shared data & alternative constructors
* **Static methods ** → helper & validation logic

This separation makes your code:

* Clean
* Scalable
* Interview‑ready

---

⭐ If this helped you, give the repo a star and keep learning 🚀
