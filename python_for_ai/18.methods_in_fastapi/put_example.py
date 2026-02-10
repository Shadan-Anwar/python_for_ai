from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="put request",
    description="this is put api development",
    version="1.0.0."
)

item_db = {1: {"name": "Car", "description": "car is good",
               "price": 2500, "is_offer": False}}


class Item(BaseModel):
    name: str
    description: str
    price: float
    is_offer: bool


@app.put("/update/{item_id}")
def update_item(item_id: int, item: Item):

    if item_id not in item_db:
        raise HTTPException(status_code=404, detail="data not found")

    item_db[item_id] = item.dict()

    return {"item_id": item_id, **item.dict()}


if __name__ == "__main__":
    uvicorn.run(
        "put_example:app",
        host="127.0.0.1",
        port=8002,
        reload=True
    )
