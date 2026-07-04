from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.database import Base

student_course = Table(
    "student_courses",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.student_id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.course_id"), primary_key=True)
)

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, index=True, nullable=False)
    credits = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teachers.teacher_id"))

    teacher = relationship("Teacher", back_populates="courses")
    students = relationship("Student", secondary=student_course, back_populates="courses")
    exams = relationship("Exam", back_populates="course")
