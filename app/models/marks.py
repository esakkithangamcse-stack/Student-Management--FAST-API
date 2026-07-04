from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Marks(Base):
    __tablename__ = "marks"

    marks_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    exam_id = Column(Integer, ForeignKey("exams.exam_id"))
    marks = Column(Integer)
    grade = Column(String)

    student = relationship("Student", back_populates="marks")
    exam = relationship("Exam", back_populates="marks")
