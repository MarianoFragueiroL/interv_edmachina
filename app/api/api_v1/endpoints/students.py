from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas.student import Students, StudentCreate, StudentDetails, StudentUpdate
from app.crud.students import create_student as create_student, fetch_students, delete_student, update_student, fetch_student
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Students)
def create_student_endpoint(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        return create_student(db, student)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/", response_model=List[Students])
def get_students_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return fetch_students(db, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.put("/{student_id}", response_model=StudentDetails)
def update_student_endpoint(student_id: int, student_update: StudentUpdate, db: Session = Depends(get_db)):
     return update_student(db, student_id, student_update)


@router.delete("/{student_id}", response_model=dict)
def remove_student_endpoint(student_id: int, db: Session = Depends(get_db)):
    try:
        delete_student(db, student_id)
        return {"message": "Student deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/{student_id}", response_model=StudentDetails)
def get_student_endpoint(student_id: int, db: Session = Depends(get_db)):
    try:
        student = fetch_student(db, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
