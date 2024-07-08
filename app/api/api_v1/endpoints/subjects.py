from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.schemas.subject import Subject, SubjectCreate
from app.crud.subjects import create_subject as crud_create_subject, fetch_subjects, delete_subject
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Subject)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    return crud_create_subject(db, subject)

@router.get("/", response_model=List[Subject])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return fetch_subjects(db, skip=skip, limit=limit)

@router.delete("/{subject_id}", response_model=dict)
def remove_subject(subject_id: int, db: Session = Depends(get_db)):
    delete_subject(db, subject_id)
    return {"message": "Subject deleted successfully"}
