from typing import List, Optional
from pydantic import BaseModel

class Subject(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    subjects: List[Subject] = []

    class Config:
        orm_mode = True
