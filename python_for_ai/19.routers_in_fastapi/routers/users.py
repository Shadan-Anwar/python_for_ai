
# import router
from fastapi import FastAPI, APIRouter, HTTPException

# create router object

router = APIRouter()

# create api using router instead of app


@router.get("/users")
def get_users():
    return {"users": ["Ali", "Ahmad", "Sara"]}


@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
