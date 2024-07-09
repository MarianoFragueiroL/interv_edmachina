from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime, timezone

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    address = Column(String, index=True)
    phone = Column(String, index=True)
    career = Column(String, index=True)
    enrollment_year = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    subject_repeats = Column(Integer, index=True)
    subjects = relationship('Subject', secondary='student_subject', back_populates='students')

    @property
    def course_time(self):
        current_year = datetime.utcnow().year
        return current_year - self.enrollment_year.year if self.enrollment_year else None