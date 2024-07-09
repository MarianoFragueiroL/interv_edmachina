from sqlalchemy import Column, Integer, String
from app.db.base import Base
from sqlalchemy.orm import relationship

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    students = relationship('Student', secondary='student_subject', back_populates='subjects')