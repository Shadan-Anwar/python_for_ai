from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="methods api",
    description="get , post, put, delete api development",
    version="1.0.0."
)

item_db = {}


class Item(BaseModel):
    name: str
    desciption: str
    price: float
    is_offer: bool


@app.post("/items/")
def cart_item(item: Item):
    item_id = len(item_db) + 1
    item_db[item_id] = item.model_dump()
    # print("list:", item_db)

    return {"item_id": item_id, **item.model_dump()}


if __name__ == "__main__":
    uvicorn.run(
        "post_example:app",
        host="127.0.0.1",
        port=8001,
        reload=True
    )
