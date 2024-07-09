from pydantic import BaseModel
from datetime import date

class StudentSubjectBase(BaseModel):
    student_id: int
    subject_id: int
    enrollment_date: date

    class Config:
        orm_mode = True

class StudentSubjectCreate(StudentSubjectBase):
    pass

class StudentSubject(StudentSubjectBase):
    class Config:
        orm_mode = True
