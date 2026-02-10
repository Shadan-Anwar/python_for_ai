# # import librarries
# from fastapi import FastAPI, HTTPException
# import uvicorn

# # import router folder here
# from routers import users
# from routers import shop_item_router


# app = FastAPI(
#     title="router",
#     description="router learning",
#     version="1.0.0"
# )

# # include router into main app
# app.include_router(
#     users.router,
#     prefix="/api",
#     tags=["Users"]
# )


# @app.get("/hello_users")
# def root_read():
#     return {"message": "hello api"}


# @app.get("/greets")
# def greeting():
#     return {"message": "Welcome all of you in fastapi"}


# if __name__ == "__main__":
#     uvicorn.run(
#         "main:app",
#         host="127.0.0.1",
#         port=8006,
#         reload=True
#     )


# import librarries
from fastapi import FastAPI, HTTPException
import uvicorn

# import router folder here
# from routers import shop_item_router
from routers import student_router


app = FastAPI(
    title="router",
    description="router learning",
    version="1.0.0"
)

# include router into main app
app.include_router(
    # shop_item_router.items_router,
    student_router.student_router,
    prefix="/api",
    tags=["Shop items"]
)


@app.get("/")
def read_root():
    return {"message": "hello api shop demo"}


@app.get("/about")
def about():
    return {"message": "Welcome to our online shop demo"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8006,
        reload=True
    )
