from pydantic import BaseModel
from typing import List
from app.schemas.subject import Subject

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    subjects: List[Subject] = []

    class Config:
        orm_mode = True
