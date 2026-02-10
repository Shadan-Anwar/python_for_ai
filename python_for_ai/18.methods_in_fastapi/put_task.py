
# Question 3 — PUT(medium)
# Create a PUT / items/{item_id} API that:
# Updates an existing item
# If item_id does not exist → return 404
# If exists → replace old data with new data
# Focus:
# Checking if item_id not in items_db
# Updating dict value


import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

item_db = {1: {"name": "car", "price": 10}, 2: {"name": "pen", "price": 20}}

app = FastAPI()


class Items(BaseModel):
    name: str
    price: float


@app.put("/items/{items_id}")
def update_items(items_id: int, item: Items):

    if items_id not in item_db:
        raise HTTPException(status_code=404, detail="Item not found")

    item_db[items_id] = item.model_dump()

    return {"items_id": items_id, **item.model_dump()}


if __name__ == "__main__":
    uvicorn.run(
        "put_task:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
