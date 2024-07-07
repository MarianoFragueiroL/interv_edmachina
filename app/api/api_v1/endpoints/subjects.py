from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.subject import Subject, SubjectCreate
from app.crud.subjects import create_subject as crud_create_subject, get_subjects, delete_subject

router = APIRouter()

@router.post("/", response_model=Subject)
def create_subject(subject: SubjectCreate):
    return crud_create_subject(subject)

@router.get("/", response_model=List[Subject])
def read_subjects():
    return get_subjects()

@router.delete("/{subject_id}", response_model=dict)
def remove_subject(subject_id: int):
    delete_subject(subject_id)
    return {"message": "Subject deleted successfully"}