from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="methods api",
    description="get  post, put, delete api development",
    version="1.0.0."
)


@app.get("/")
def read_root():
    return {"message": "hello fast api "}


if __name__ == "__main__":
    uvicorn.run(
        "get_example:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
