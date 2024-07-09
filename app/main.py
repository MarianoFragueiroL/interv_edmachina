from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.api.api_v1.api import api_router
from app.db.session import engine, Base

def init_db():
    Base.metadata.create_all(bind=engine)

def create_app() -> FastAPI:
    app = FastAPI()
    init_db()

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder({"detail": exc.errors()}),
        )

    app.include_router(api_router, prefix="/api")

    return app

app = create_app()

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI project!"}
