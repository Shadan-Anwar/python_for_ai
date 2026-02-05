
# Create a POST API that accepts a sentence and returns some processed data.

from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn

"""
File Name: first_app.py
Author: Shadan Anwar
Description:
    A professionally structured FastAPI application demonstrating
    Python fundamentals, API development, request/response modeling,
    validation, and real-world backend logic.

Purpose:
    This file is part of the Python-for-AI & Backend learning journey.
    It is designed to help beginners transition into confident,
    production-ready API developers.

Topics Covered:
    - Python basics & execution flow
    - FastAPI fundamentals
    - Request & Response Models (Pydantic)
    - POST APIs
    - Validation & error handling
    - Real-world API patterns
    - Clean, readable, professional coding standards
"""

# ============================================================
# 🧠 WHAT IS PYTHON?
# ============================================================

"""
Python is a high-level, interpreted, general-purpose programming language.

Why Python?
- Easy to read and write (English-like syntax)
- Rapid development
- Cross-platform
- Massive ecosystem
- Dominates AI, ML, Data Science & Backend development

Why Python is powerful for APIs & AI:
- Clean syntax reduces cognitive load
- Strong typing support (with Pydantic)
- Fast prototyping
- Excellent community support
"""

# ============================================================
# 📦 IMPORTS
# ============================================================


"""
Explanation:
- FastAPI        → Web framework for building APIs
- HTTPException → Used to return HTTP error responses
- BaseModel     → Used to define request & response schemas
- Optional      → Allows optional fields
- uvicorn       → ASGI server to run the FastAPI app
"""

# ============================================================
# 🚀 FASTAPI APP INITIALIZATION
# ============================================================

app = FastAPI(
    title="FastAPI Learning APIs",
    description="A collection of beginner to advanced FastAPI examples",
    version="1.0.0"
)

# ============================================================
# 🏠 ROOT ENDPOINT (HEALTH CHECK)
# ============================================================


@app.get("/")
def home():
    """
    Health check endpoint.
    Used to verify the API is running.
    """
    return {"message": "FastAPI is running successfully 🚀"}

# ============================================================
# ✅ QUESTION 1 — TEXT ANALYZER
# ============================================================


"""
Task:
Create a POST API that accepts a sentence and returns processed data.

Logic:
- Accept a sentence
- Optionally reverse it
- Count total words
"""


class TextAnalyzeRequest(BaseModel):
    sentence: str
    reverse: Optional[bool] = False


class TextAnalyzeResponse(BaseModel):
    processed_text: str
    total_count: int


@app.post("/analyze-text", response_model=TextAnalyzeResponse)
def analyze_text(request: TextAnalyzeRequest):

    if not request.sentence.strip():
        raise HTTPException(
            status_code=400,
            detail="Sentence must not be empty"
        )

    processed_text = (
        request.sentence[::-1]
        if request.reverse
        else request.sentence
    )

    word_count = len(processed_text.split())

    return TextAnalyzeResponse(
        processed_text=processed_text,
        total_count=word_count
    )

# ============================================================
# ✅ QUESTION 2 — TEXT FORMATTER
# ============================================================


"""
Task:
Format text with optional capitalization.
"""


class FormatTextRequest(BaseModel):
    text: str
    capitalize: Optional[bool] = False


class FormatTextResponse(BaseModel):
    final_text: str
    character_count: int


@app.post("/format-text", response_model=FormatTextResponse)
def format_text(request: FormatTextRequest):

    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty"
        )

    final_text = (
        request.text.capitalize()
        if request.capitalize
        else request.text
    )

    return FormatTextResponse(
        final_text=final_text,
        character_count=len(final_text)
    )

# ============================================================
# ✅ QUESTION 3 — AGE VALIDATOR
# ============================================================


"""
Task:
Validate user age and determine Minor or Adult.
"""


class AgeCheckRequest(BaseModel):
    name: str
    age: int


class AgeCheckResponse(BaseModel):
    name: str
    status: str


@app.post("/check-age", response_model=AgeCheckResponse)
def check_age(request: AgeCheckRequest):

    if not request.name.strip():
        raise HTTPException(
            status_code=400,
            detail="Name cannot be empty"
        )

    if request.age < 0:
        raise HTTPException(
            status_code=400,
            detail="Age cannot be negative"
        )

    status = "Adult" if request.age >= 18 else "Minor"

    return AgeCheckResponse(
        name=request.name,
        status=status
    )

# ============================================================
# ✅ QUESTION 4 — PASSWORD STRENGTH CHECKER
# ============================================================


"""
Task:
Check if a password is strong based on minimum length.
"""


class PasswordRequest(BaseModel):
    password: str
    min_length: Optional[int] = 8


class PasswordResponse(BaseModel):
    is_strong: bool
    password_length: int


@app.post("/check-password", response_model=PasswordResponse)
def check_password(request: PasswordRequest):

    if not request.password:
        raise HTTPException(
            status_code=400,
            detail="Password cannot be empty"
        )

    is_strong = len(request.password) >= request.min_length

    return PasswordResponse(
        is_strong=is_strong,
        password_length=len(request.password)
    )

# ============================================================
# ✅ QUESTION 5 — SHOPPING CART SUMMARY
# ============================================================


"""
Task:
Summarize shopping cart with optional discount.
"""


class CartRequest(BaseModel):
    items: List[str]
    apply_discount: Optional[bool] = False


class CartResponse(BaseModel):
    total_items: int
    final_price: int


@app.post("/cart-summary", response_model=CartResponse)
def cart_summary(request: CartRequest):

    if not request.items:
        raise HTTPException(
            status_code=400,
            detail="Item list cannot be empty"
        )

    price_per_item = 100
    total_price = len(request.items) * price_per_item

    if request.apply_discount:
        total_price = int(total_price * 0.9)  # 10% discount

    return CartResponse(
        total_items=len(request.items),
        final_price=total_price
    )

# ============================================================
# ✅ QUESTION 6 — LOGIN SIMULATOR
# ============================================================


"""
Task:
Simulate a login process.
"""


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    username: str
    message: str


@app.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):

    if not request.username.strip():
        raise HTTPException(
            status_code=400,
            detail="Username cannot be empty"
        )

    if not request.password:
        raise HTTPException(
            status_code=400,
            detail="Password cannot be empty"
        )

    message = (
        "Login Failed"
        if len(request.password) < 6
        else "Login Successful"
    )

    return LoginResponse(
        username=request.username,
        message=message
    )

# ============================================================
# ▶️ APPLICATION ENTRY POINT
# ============================================================


if __name__ == "__main__":
    uvicorn.run(
        "fastapi_learning_journey:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
