from typing import List
from pydantic import BaseModel
from .subject import Subject

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    subjects: List[int] = []

class Student(StudentBase):
    id: int
    subjects: List[Subject] = []

    class Config:
        orm_mode = True