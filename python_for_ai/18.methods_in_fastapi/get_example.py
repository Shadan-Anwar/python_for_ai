from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="methods api",
    description="get , post, put, delete api development",
    version="1.0.0."
)


@app.get("/")
def read_root():
    return {"message": "hello fast api "}

# # fake db
# card_db = []

# # card item


# class CardItem(BaseModel):
#     id: int
#     product_name: str
#     quantity: int
#     price: float


# @app.get("/cart/{item_id}")
# def get_cart_item(item_id: int):

#     for item in card_db:
#         if item["id"] == item_id:
#             return item
#         raise HTTPException(status_code=404, detail="Item not found")


# if __name__ == "__main__":
#     uvicorn.run(
#         "get_example:app",
#         host="127.0.0.1",
#         port=8000,
#         reload=True
#     )
