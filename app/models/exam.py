from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Exam(Base):
    __tablename__ = "exams"

    exam_id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    exam_name = Column(String, nullable=False)
    date = Column(Date, nullable=False)

    course = relationship("Course", back_populates="exams")
    marks = relationship("Marks", back_populates="exam")
