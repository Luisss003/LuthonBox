from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="LuthonBox")

app.include_router(router)

@app.get("/ping")
def ping():
    return {"message": "pong"}

