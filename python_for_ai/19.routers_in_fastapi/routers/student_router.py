"""
File Name: student_router.py
Author: Shadan Anwar

Description:
A professionally structured FastAPI router module that demonstrates
how to design RESTful APIs using APIRouter, Pydantic models, and
an in-memory database.

Purpose:
This file is part of the FastAPI learning journey.
It focuses on:
- Understanding APIRouter
- Request & response models
- Clean API design
- Professional documentation style for GitHub

Deep Explanation of new_id logic:

Expression:
new_id = max(student_db.keys()) + 1 if student_db else 201

Step-by-step:

1. student_db.keys()
   → Returns all existing student IDs

2. max(student_db.keys())
   → Finds the highest existing ID

3. * 1
     → Generates next unique ID

4. if student_db
   → Checks whether database is empty

5. else 201
   → Default starting ID if no data exists

This is called a *ternary conditional expression*.

Why st_data.dict()?
- Converts Pydantic model into plain dictionary
- Required for storing data in normal Python structures
"""

# =====================================================

# END OF FILE

# =====================================================

"""
Key Takeaways:

✔ Clean project structure using routers
✔ Strong validation using Pydantic
✔ Professional API responses
✔ Scalable design pattern

Next Steps:
- Integrate this router into main.py
- Replace fake DB with PostgreSQL
- Add PUT and DELETE APIs
"""


# ============================================================
# Students Management Router (FastAPI)
# ============================================================

# -------------------- Imports --------------------
from typing import Dict, List, Union
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


# -------------------- Router --------------------
# This router represents the "Students" feature/module
# It will be included in the main FastAPI app using include_router()
student_router = APIRouter()


# -------------------- Fake Database --------------------
# In-memory database (for learning/demo only)
# Key   -> student_id (int)
# Value -> student details (dict)
student_db: Dict[int, Dict[str, Union[str, int]]] = {
    1: {"name": "shaddy", "age": 29, "course": "ai"},
    2: {"name": "anwar", "age": 30, "course": "python"},
}


# -------------------- Pydantic Models --------------------
class Student(BaseModel):
    """
    Request model:
    Used when creating a new student.
    Defines what data the client must send.
    """
    name: str
    age: int
    course: str


class StudentWithId(Student):
    """
    Response model:
    Extends Student by adding student_id.
    Used in API responses.
    """
    student_id: int


# -------------------- GET: All Students --------------------
@student_router.get(
    "/",
    response_model=Dict[str, Union[str, List[StudentWithId]]]
)
def get_all_students():
    """
    Fetch all students along with their IDs.
    """

    # Convert database dictionary into a list of students
    # Each student includes student_id + student details
    students = [
        {"student_id": student_id, **student_data}
        for student_id, student_data in student_db.items()
    ]

    return {
        "message": "All student records fetched successfully",
        "students": students,
    }


# -------------------- GET: Student by ID --------------------
@student_router.get(
    "/{student_id}",
    response_model=StudentWithId
)
def get_student_by_id(student_id: int):
    """
    Fetch a single student using student_id.
    """

    if student_id in student_db:
        return {
            "student_id": student_id,
            **student_db[student_id]
        }

    # If student_id does not exist, raise a 404 error
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# -------------------- POST: Create Student --------------------
@student_router.post(
    "/",
    response_model=Dict[str, Union[str, StudentWithId]]
)
def create_student(student: Student):
    """
    Create a new student and assign a unique student_id.
    """

    # Generate a new student ID
    # If database has data -> max ID + 1
    # If database is empty -> start from 201
    new_id = max(student_db.keys()) + 1 if student_db else 201

    # Store student data in the database
    student_db[new_id] = student.dict()

    return {
        "message": "Student created successfully",
        "student": {
            "student_id": new_id,
            **student.dict()
        }
    }
