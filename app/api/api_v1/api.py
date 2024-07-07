from fastapi import APIRouter
from app.api.api_v1.endpoints import students, subjects

api_router = APIRouter()
api_router.include_router(students.router, prefix="/students", tags=["students"])
api_router.include_router(subjects.router, prefix="/subjects", tags=["subjects"])
