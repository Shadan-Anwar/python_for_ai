from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from src.routers.data_handler import router
from pydantic import BaseModel
import uvicorn


app = FastAPI(
    title="fastapi for chat with pdf",
    description="chat with pdf using fastapi router",
    version="0.1.0"
)

app.include_router(
    router,
    prefix="/api/v1",
    tags=["Data handling and chat with pdf"]
)

# app.include_router(
#     data_handler.router,
#     prefix="/api/v1",
#     tags=['Data handling and chat with pdf']
# )


@app.get("/", response_class=HTMLResponse, tags=["Root"])
def read_root():
    html_content = """
    <h1>Hello chat with pdf</h1>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/hello")
def greeting():
    return {"message": "Hello fast api"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8006,
        reload=True
    )
