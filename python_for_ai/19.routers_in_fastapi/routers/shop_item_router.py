# # import libraries
# from fastapi import FastAPI, HTTPException, APIRouter
# from pydantic import BaseModel
# from typing import Dict, List, Union


# # create app
# items_router = APIRouter()

# items_data: Dict[int, Dict] = {
#     1: {"name": "car", "price": 2000}, 2: {"name": "bike", "price": 1000}
# }

# # item_db = {1: {"name": "car", "price": 20}, 2: {"name": "bike", "price": 10}}


# class Items_data(BaseModel):
#     name: str
#     price: float


# class Item_with_Id(Items_data):
#     item_id: int


# # define jobs endpoint with departments
# @items_router.get("/", response_model=Dict[str, Union[str, List[Item_with_Id]]])
# def get_items_list():

#     items_list_with_ids = [{"item_id": item_id, **item_data}
#                            for item_id, item_data in items_data.items()]
#     return {"message": "here are the all items in our shop", "items": items_list_with_ids}


# # get a specific item by its id
# @items_router.get("/{itemID}", response_model=Item_with_Id)
# def get_item_with_id(itemID: int):

#     if itemID in items_data:
#         return {"item_id": itemID, **items_data[itemID]}
#     raise Exception(status_code=404, detail="Data not found")

# # Add a new item in this list


# @items_router.post("/", response_model=Dict[str, Union[str, int, Items_data]])
# # @items_router.post("/", response_model=Dict[str, Union[str, int, Item]])
# def create_new_item(item: Items_data):
#     # Add brand new item to our shop
#     new_id = max(items_data.keys()) + 1 if items_data else 201
#     items_data[new_id] = item.dict()
#     return {"message": f"Item adds {item.name} successfully", "item_id": new_id, **item.dict()}


from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Dict, Union

# create router
items_router = APIRouter()

# create db
item_db: Dict[int, Dict] = {
    1: {"name": "car", "price": 100}, 2: {"name": "bike", "price": 50}
}

# define module for request


class Item(BaseModel):
    name: str
    price: int

# define another model for item_id


class Item_with_id(Item):
    item_id: int

# get all list of item data


@items_router.get("/", response_model=Dict[str, Union[str, List[Item_with_id]]])
def get_list():
    item_data_with_list = [{"item_id": item_id, **item_db}
                           for item_id, item_db in item_db.items()]

    return {"message": "all_items_data", "items": item_data_with_list}


# get data by specific id
@items_router.get("/{item_id}", response_model=Item_with_id)
def get_item_with_id(item_id: int):

    if item_id in item_db:
        return {"item_id": item_id, **item_db[item_id]}
    raise HTTPException(status_code=404, detail="Data not found")

# post create item


@items_router.post("/", response_model=Dict[str, Union[str, int, Item]])
def post_item_data(item: Item):
    new_id = max(item_db.keys()) + 1 if item_db else 201
    item_db[new_id] = item.dict()
    return {"message": "item added successfully", "item_id": new_id, **item.dict()}
