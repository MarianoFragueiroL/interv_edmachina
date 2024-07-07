from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.student import Student, StudentCreate
from app.crud.students import create_student as crud_create_student, get_students

router = APIRouter()

@router.post("/", response_model=Student)
def create_student(student: StudentCreate):
    return crud_create_student(student)

@router.get("/", response_model=List[Student])
def read_students():
    return get_students()
