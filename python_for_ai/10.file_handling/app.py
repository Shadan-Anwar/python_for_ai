"""
===========================================================
Python File Handling & JSON Handlings
Author : Shadan Anwar
Purpose: Learn read, write, append, rewrite & JSON operations
===========================================================
"""

import json

# ----------------------------------------------------------
# FILE PATHS
# ----------------------------------------------------------
file_path = "File.txt"      # Existing / main file
file_paths = "Filess.txt"   # File that may or may not exist


# ==========================================================
# 1️⃣ WRITE MODE ("w")
# ==========================================================
"""
'w' MODE:
- Creates a new file if it does not exist
- If file exists → ERASES old content
- Write only (cannot read)
"""

with open(file_path, "w") as file:
    # Writing first line
    file.write("Hello python i am creating a file\n")

    # Writing second line
    file.write("My name is Shaddy just start learning python for AI\n")

# File is AUTO-CLOSED here (because of 'with')


# -------------------- EXTRA EXAMPLES (WRITE) --------------------

# Example 1: Writing numbers
with open("numbers.txt", "w") as file:
    file.write("1\n2\n3\n4\n5")

# Example 2: Writing user input
user_name = "Shaddy"
with open("user.txt", "w") as file:
    file.write(f"User name is: {user_name}")


# ==========================================================
# 2️⃣ READ MODE ("r")
# ==========================================================
"""
'r' MODE:
- Reads file content
- File MUST exist
- Cursor starts from beginning
"""

with open(file_path, "r") as file:
    content = file.read()
    print("Content from file:\n", content)


# -------------------- EXTRA EXAMPLES (READ) --------------------

# Example 1: Read line by line
with open(file_path, "r") as file:
    for line in file:
        print("Line:", line.strip())

# Example 2: Read limited characters
with open(file_path, "r") as file:
    print("First 10 chars:", file.read(10))


# ==========================================================
# 3️⃣ APPEND + READ MODE ("a+")
# ==========================================================
"""
'a+' MODE:
- Appends data at the END of file
- Does NOT delete existing data
- Cursor stays at end after write
- Use seek(0) to read from beginning
"""

with open(file_path, "a+") as file:
    # Appending new content
    file.write("This is appending text, i am adding here in existing file.\n")

    # Move cursor back to beginning to READ
    file.seek(0)

    all_cont = file.read()
    print("All content after append:\n", all_cont)


# -------------------- EXTRA EXAMPLES (APPEND) --------------------

# Example 1: Log file
with open("log.txt", "a+") as file:
    file.write("User logged in\n")

# Example 2: Append and verify
with open("data.txt", "a+") as file:
    file.write("New record added\n")
    file.seek(0)
    print(file.read())


# ==========================================================
# 4️⃣ READ FILE WITH ERROR HANDLING (try-except)
# ==========================================================
"""
WHY try-except?
- File may not exist
- Permission issues
- Prevent program crash
"""

try:
    with open(file_paths, "r") as file:
        file.seek(0)
        all_content = file.read()
        print("All content:\n", all_content)

except Exception as e:
    print("Error occurred while reading file:", e)


# -------------------- EXTRA EXAMPLES (ERROR HANDLING) --------------------

# Example 1: Catch specific error
try:
    with open("abc.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")

# Example 2: Print real error message
try:
    with open("abc.txt", "r") as file:
        print(file.read())
except Exception as e:
    print("Actual error:", e)


# ==========================================================
# 5️⃣ JSON FILE HANDLING
# ==========================================================
"""
JSON:
- Used in APIs, AI configs, databases
- Stored as key-value pairs
"""

data = {
    "name": "Shaddy",
    "age": 28,
    "course": "python"
}

# -------------------- WRITE JSON --------------------
with open("data.json", "w") as file:
    # json.dump converts Python dict → JSON
    json.dump(data, file, indent=4)


# -------------------- READ JSON --------------------
try:
    with open("datas.json", "r") as file:
        content = json.load(file)
        print("JSON Content:", content)

except Exception as e:
    print("Error occurred in json format:", e)


# -------------------- EXTRA EXAMPLES (JSON) --------------------

# Example 1: Read and access value
with open("data.json", "r") as file:
    data = json.load(file)
    print("Name from JSON:", data["name"])

# Example 2: Update JSON
data["age"] = 29
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


# ==========================================================
# END OF FILE
# ==========================================================
