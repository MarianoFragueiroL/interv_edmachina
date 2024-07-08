from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.db.session import engine, Base

def init_db():
    Base.metadata.create_all(bind=engine)

def create_app() -> FastAPI:
    app = FastAPI()
    init_db()

    app.include_router(api_router, prefix="/api")

    return app

app = create_app()

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI project!"}