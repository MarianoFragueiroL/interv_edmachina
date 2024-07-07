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

def get_subjects_by_ids(subject_ids: List[int]) -> List[Subject]:
    return [subject for subject in subjects_db if subject.id in subject_ids]

def delete_subject(subject_id: int) -> None:
    global subjects_db
    subjects_db = [s for s in subjects_db if s.id != subject_id]