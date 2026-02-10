# Question 4 — DELETE(medium)

# Create a DELETE / items/{item_id} API that:
# Deletes the item from items_db
# Returns message "Item deleted successfully"
# If item doesn’t exist → return 404
# Focus:
# del items_db[item_id]
# Safe deletion


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn


item_db = {1: {"name": "car", "price": 10}, 2: {"name": "pen", "price": 20}}

app = FastAPI()


class Items(BaseModel):
    name: str
    price: float


@app.put("/items/{items_id}")
def update_items(items_id: int):

    if items_id not in item_db:
        raise HTTPException(status_code=404, detail="Item not found")

    # item_db[items_id] = item.model_dump()
    del item_db[items_id]

    return {"items_id": items_id, "message": "item deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(
        "del_task:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
