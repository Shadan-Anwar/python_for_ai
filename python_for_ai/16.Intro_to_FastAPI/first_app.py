
"""
File Name: first_app.py
Author: Shadan Anwar
Project: Hello World FastAPI Application
Version: 1.0.0

Description:
    This project is a beginner-friendly FastAPI application that demonstrates
    how to build, run, and understand a simple REST API using modern Python tools.

    The application exposes two HTTP GET endpoints:
    1. A home route ("/") that returns a welcome message
    2. A dynamic route ("/user/{name}") that accepts user input via the URL

Purpose:
    This project is part of my API and backend learning journey.
    It focuses on understanding:
        - What an API is
        - How HTTP requests and responses work
        - How FastAPI handles routing and validation
        - How to run an API server using Uvicorn

What is FastAPI?

    FastAPI is a modern, high-performance Python web framework used to build APIs.

    It is designed for:
        - Speed (very fast execution)
        - Developer productivity
        - Automatic documentation
        - Built-in data validation

Key Features of FastAPI:
    - Easy to learn and use
    - Based on Python type hints
    - Automatic request validation
    - Auto-generated Swagger UI & ReDoc
    - High performance (built on Starlette & Pydantic)

What is an API?

    API stands for Application Programming Interface.

    An API allows:
        - One application to talk to another
        - Clients (browser, mobile app, frontend) to request data
        - Servers to respond with structured data (usually JSON)

How This API Works (Request → Response Flow):

    1. A client sends an HTTP request (GET request)
    2. FastAPI matches the request to a route
    3. The corresponding Python function is executed
    4. The function returns data (dictionary)
    5. FastAPI automatically converts it into JSON
    6. The response is sent back to the client

About Routes Used in This Project:

    "/" 
        - Home route
        - Returns a welcome message
        - Used to check if the API is running

    "/user/{name}"
        - Dynamic route
        - Accepts 'name' as a path parameter
        - Returns a personalized greeting message

What is Uvicorn?

    Uvicorn is an ASGI server used to run FastAPI applications.

    It:
        - Starts the web server
        - Listens for incoming HTTP requests
        - Sends requests to FastAPI
        - Returns responses to the client

How to Run This Application:

    Run the file using:
        python first_app.py

    API will be available at:
        http://127.0.0.1:8000

    Interactive API Documentation:
        Swagger UI → http://127.0.0.1:8000/docs
        ReDoc       → http://127.0.0.1:8000/redoc

Learning Outcome:
    By building this project, I learned:
        - Basic FastAPI setup
        - API routing concepts
        - Path parameters
        - JSON responses
        - Running APIs using Uvicorn
        - Understanding request-response lifecycle
"""


# ==============================
# Import required libraries
# ==============================

# FastAPI is the main class used to create an API application
from fastapi import FastAPI

# Uvicorn is an ASGI server used to run FastAPI applications
import uvicorn


# ==============================
# Create FastAPI application object
# ==============================

# Here we are creating an instance of the FastAPI class
# This 'app' object will handle all API requests
app = FastAPI(
    title="Hello World API",            # Title shown in Swagger UI
    description="This is my first API",  # Description shown in docs
    version="1.0.0"                     # API version
)


# ==============================
# Define Home Route
# ==============================

# @app.get("/") is a decorator
# It tells FastAPI:
# "When a GET request comes to '/', call the function below"
@app.get("/")
# This function will be executed when the "/" endpoint is accessed
def hello_world():
    # FastAPI automatically converts Python dict to JSON
    return {"message": "Welcome to FastAPI"}


# ==============================
# Define Dynamic Route with Path Parameter
# ==============================

# This route accepts a dynamic value called 'name'
# Example URL: /user/Shadan
@app.get("/user/{name}")
# 'name: str' means:
# - name is required
# - name must be a string
# FastAPI automatically validates this
def user_name(name: str):
    return {"message": f"Hello, {name}"}


# ==============================
# Run the application using Uvicorn
# ==============================

# This condition checks:
# "Is this file being run directly?"
if __name__ == "__main__":

    # uvicorn.run() starts the server
    # "first_app:app" means:
    #   - first_app → filename (without .py)
    #   - app → FastAPI instance
    uvicorn.run(
        "first_app:app",
        host="127.0.0.1",  # Localhost
        port=8000,         # Port number
        reload=True        # Auto-restart on code changes
    )
