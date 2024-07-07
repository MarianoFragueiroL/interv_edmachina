from fastapi import HTTPException
from typing import List
from app.models.student import Student
from app.schemas.student import StudentCreate
from app.crud.subjects import get_subjects_by_ids

students_db = []

def create_student(student: StudentCreate) -> Student:
    new_student = Student(id=len(students_db) + 1, **student.dict())
    students_db.append(new_student)
    return new_student

def get_students() -> List[Student]:
    return students_db

def update_student_subjects(student_id: int, subject_ids: List[int]) -> Student:
    student = next((s for s in students_db if s.id == student_id), None)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    subjects = get_subjects_by_ids(subject_ids)
    student.subjects = subjects
    return student

def delete_student(student_id: int) -> None:
    global students_db
    students_db = [s for s in students_db if s.id != student_id]
