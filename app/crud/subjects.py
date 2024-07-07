from typing import List
from app.models.subject import Subject
from app.schemas.subject import SubjectCreate

subjects_db = []

def create_subject(subject: SubjectCreate) -> Subject:
    new_subject = Subject(id=len(subjects_db) + 1, **subject.dict())
    subjects_db.append(new_subject)
    return new_subject

def get_subjects() -> List[Subject]:
    return subjects_db
