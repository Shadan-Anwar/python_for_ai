from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List

item_db = {1: {"name": "Shaddy", "description": "Bro",
               "price": 28, "is_offer": False}, 2: {"name": "Anwar", "description": "friend",
                                                    "price": 30, "is_offer": True}}

app = FastAPI(
    title="delete api",
    description="delete api development",
    version="1.0.0"
)


class Item(BaseModel):
    name: str
    description: str
    price: float
    is_offer: bool


@app.delete("/remove/{item_id}")
def del_item(item_id: int, item: Item):
    if item_id not in item_db:
        raise HTTPException(status_code=404, detail="File not Found")
    del item_db[item_id]

    return {"message": f"{item_id} deleted successfully:"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8003, reload=True)


if __name__ == "__main__":
    uvicorn.run(
        "delete_example:app",
        host="127.0.0.1",
        port=8003,
        reload=True
    )
