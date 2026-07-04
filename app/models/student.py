from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String)
    gender = Column(String)
    dob = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    department = relationship("Department", back_populates="students")
    profile = relationship("Profile", back_populates="student", uselist=False)
    courses = relationship("Course", secondary="student_courses", back_populates="students")
    attendances = relationship("Attendance", back_populates="student")
    marks = relationship("Marks", back_populates="student")
    fees = relationship("Fees", back_populates="student")


class Profile(Base):
    __tablename__ = "profiles"

    profile_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.student_id"), unique=True)
    address = Column(String)
    photo_url = Column(String)

    student = relationship("Student", back_populates="profile")
