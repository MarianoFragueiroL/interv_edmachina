from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

student_subject_association = Table(
    'student_subject', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('subject_id', Integer, ForeignKey('subjects.id')),
    extend_existing=True
)

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    students = relationship("Student", secondary=student_subject_association, back_populates="subjects")
