from typing import List
from app.models.student import Student
from app.schemas.student import StudentCreate

students_db = []

def create_student(student: StudentCreate) -> Student:
    new_student = Student(id=len(students_db) + 1, **student.dict())
    students_db.append(new_student)
    return new_student

def get_students() -> List[Student]:
    return students_db
