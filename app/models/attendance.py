from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Attendance(Base):
    __tablename__ = "attendances"

    attendance_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)  # e.g., Present, Absent

    student = relationship("Student", back_populates="attendances")
    course = relationship("Course")
