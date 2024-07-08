from sqlalchemy.orm import Session
from typing import List
from app.models.subject import Subject
from app.schemas.subject import SubjectCreate

def create_subject(db: Session, subject: SubjectCreate) -> Subject:
    db_subject = Subject(name=subject.name)
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def fetch_subjects(db: Session, skip: int = 0, limit: int = 10) -> List[Subject]:
    return db.query(Subject).offset(skip).limit(limit).all()

def delete_subject(db: Session, subject_id: int) -> None:
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if subject:
        db.delete(subject)
        db.commit()
