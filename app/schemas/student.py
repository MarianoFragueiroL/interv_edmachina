from typing import List, Optional
from pydantic import BaseModel, EmailStr
from .subject import Subject
from datetime import datetime


class StudentCreate(BaseModel):
    name: str
    email: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    career: Optional[str] = None
    subject_repeats: Optional[int] = None
    subjects: List[int] = []

    class Config:
        orm_mode = True

class StudentDetails(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    career: Optional[str] = None
    enrollment_year: Optional[datetime] = None
    subject_repeats: Optional[int] = None
    subjects: List[Subject] = []

    class Config:
        orm_mode = True

class Students(BaseModel):
    id: int
    name: str
    subjects: List[Subject] = []

    class Config:
        orm_mode = True