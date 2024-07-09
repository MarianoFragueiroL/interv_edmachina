from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.api.api_v1.api import api_router
from app.db.session import engine, Base
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
]
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI project!"}
