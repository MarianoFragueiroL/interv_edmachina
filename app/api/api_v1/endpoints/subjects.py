from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas.subject import Subject, SubjectCreate
from app.crud.subjects import create_subject as create_subject, fetch_subjects, delete_subject
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Subject)
def create_subject_endpoint(subject: SubjectCreate, db: Session = Depends(get_db)):
    try:
        return create_subject(db, subject)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/", response_model=List[Subject])
def get_subjects_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return fetch_subjects(db, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/{subject_id}", response_model=dict)
def remove_subject_endpoint(subject_id: int, db: Session = Depends(get_db)):
    try:
        delete_subject(db, subject_id)
        return {"message": "Subject deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
