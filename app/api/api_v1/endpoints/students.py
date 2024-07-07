from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.schemas.student import Student, StudentCreate
from app.crud.students import create_student as crud_create_student, get_students, delete_student, update_student_subjects
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return crud_create_student(db, student)

@router.get("/", response_model=List[Student])
def read_students(db: Session = Depends(get_db)):
    return get_students(db)

@router.put("/{student_id}/subjects", response_model=Student)
def add_subjects_to_student(student_id: int, subject_ids: List[int], db: Session = Depends(get_db)):
    return update_student_subjects(db, student_id, subject_ids)

@router.delete("/{student_id}", response_model=dict)
def remove_student(student_id: int, db: Session = Depends(get_db)):
    delete_student(db, student_id)
    return {"message": "Student deleted successfully"}
