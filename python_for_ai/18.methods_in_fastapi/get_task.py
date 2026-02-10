# Practice Questions (FastAPI CRUD)
# Question 1 — GET (very easy)
# You have this database:
# items_db = {
#     1: {"name": "Pen", "price": 10},
#     2: {"name": "Book", "price": 100}
# }


# Task:
# Create a GET /items/{item_id} API that:
# Returns the item if item_id exists
# Returns 404 with message "Item not found" if it doesn’t
# Focus: path parameter + dict access

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn


items_db = {1: {"name": "Pen", "price": 10}, 2: {"name": "Book", "price": 100}}

app = FastAPI(
    title="get task",
    description="fast api development",
    version="1.0.0."
)


class Items(BaseModel):
    id: int
    name: str
    price: float


@app.get("/items/{item_id}")
def get_item(item_id: int):

    if not item_id:
        raise HTTPException(status_code=404, detail="Item_id can not be empty")
    elif item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"item_id": item_id, **items_db[item_id]}


if __name__ == "__main__":
    uvicorn.run(
        "get_task:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
