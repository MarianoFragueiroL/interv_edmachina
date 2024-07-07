from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.student import Student, StudentCreate
from app.crud.students import create_student as crud_create_student, get_students, update_student_subjects, delete_student

router = APIRouter()

@router.post("/", response_model=Student)
def create_student(student: StudentCreate):
    return crud_create_student(student)

@router.get("/", response_model=List[Student])
def read_students():
    return get_students()

@router.put("/{student_id}/subjects", response_model=Student)
def add_subjects_to_student(student_id: int, subject_ids: List[int]):
    return update_student_subjects(student_id, subject_ids)

@router.delete("/{student_id}", response_model=dict)
def remove_student(student_id: int):
    delete_student(student_id)
    return {"message": "Student deleted successfully"}