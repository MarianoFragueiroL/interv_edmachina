from sqlalchemy import Column, Integer, ForeignKey, Date
from app.db.base import Base
from datetime import date

class StudentSubject(Base):
    __tablename__ = 'student_subject'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), primary_key=True)
    enrollment_date = Column(Date, default=date.today)