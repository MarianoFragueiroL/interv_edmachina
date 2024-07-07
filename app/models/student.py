from pydantic import BaseModel
from typing import List
from app.models.subject import Subject

class Student(BaseModel):
    id: int
    name: str
    subjects: List[Subject] = []
