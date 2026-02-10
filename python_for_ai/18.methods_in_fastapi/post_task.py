# Question 2 — POST (easy)

# Create a POST /items/ API that:

# Accepts an Item model (name, price)

# Generates a new item_id

# Stores the item using item.model_dump()

# Returns the new item_id along with item data

# Focus: why we use model_dump()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

item_db = {}

app = FastAPI()


class RequestItems(BaseModel):
    name: str
    price: float

# class ResponseItems(BaseModel):


@app.post("/items")
def post_item(item: RequestItems):
    item_id = len(item_db) + 1
    item_db[item_id] = item.model_dump()

    return {"Item_id": item_id, **item.model_dump()}


if __name__ == "__main__":
    uvicorn.run(
        "post_task:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
