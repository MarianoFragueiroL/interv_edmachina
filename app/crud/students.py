from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.student import Student
from app.schemas.student import StudentCreate
from app.models.subject import Subject

def create_student(db: Session, student: StudentCreate) -> Student:
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session) -> List[Student]:
    return db.query(Student).all()

def update_student_subjects(db: Session, student_id: int, subject_ids: List[int]) -> Student:
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    subjects = db.query(Subject).filter(Subject.id.in_(subject_ids)).all()
    student.subjects = subjects
    db.commit()
    db.refresh(student)
    return student

def delete_student(db: Session, student_id: int) -> None:
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
