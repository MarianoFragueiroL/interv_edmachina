from typing import List
from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    students: List[Student] = []

    class Config:
        orm_mode = True
