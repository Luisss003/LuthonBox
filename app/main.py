from routes import router
from fastapi import FastAPI

app = FastAPI(title="LuthonBox - Malware Analysis")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "LuthonBox is running"}
