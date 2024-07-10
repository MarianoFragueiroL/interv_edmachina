from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.models.student import Student
from app.models.subject import Subject
from app.schemas.student import StudentCreate, StudentDetails, StudentUpdate
from datetime import datetime, timezone
from app.models.student_subject import StudentSubject


def create_student(db: Session, student: StudentCreate) -> Student:
    try:
        db_student = Student(
            name=student.name,
            email=student.email,
            address=student.address,
            phone=student.phone,
            career=student.career,
            enrollment_year=datetime.now(timezone.utc),
            subject_repeats=student.subject_repeats,
        )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)

        if student.subjects:
            for subject_id in student.subjects:
                subject = db.query(Subject).filter(Subject.id == subject_id).first()
                if subject:
                    db_student_subject = StudentSubject(student_id=db_student.id, subject_id=subject_id)
                    db.add(db_student_subject)
            db.commit()

        db.refresh(db_student)
        return db_student
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def fetch_students(db: Session, skip: int = 0, limit: int = 10) -> List[Student]:
    students = db.query(Student).offset(skip).limit(limit).all()
    return students

def update_student(db: Session, student_id: int, student_update: StudentUpdate) -> StudentDetails:
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            return False

        update_data = student_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            if key != "subjects":
                setattr(student, key, value)

        if "subjects" in update_data:
            subject_ids = update_data["subjects"]
            db.query(StudentSubject).filter(StudentSubject.student_id == student_id).delete()
            if subject_ids:
                for subject_id in subject_ids:
                    student_subject = StudentSubject(student_id=student_id, subject_id=subject_id)
                    db.add(student_subject)

        db.commit()
        db.refresh(student)
        return student

def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    print(student)
    if student:
        db.delete(student)
        db.commit()
        return True
    return False

def fetch_student(db: Session, student_id: int) :
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        return None

    student.subjects = db.query(Subject).join(StudentSubject).filter(StudentSubject.student_id == student_id).all()
    return student