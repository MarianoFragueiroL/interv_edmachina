from fastapi import FastAPI
from app.api.api_v1.api import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI project!"}
