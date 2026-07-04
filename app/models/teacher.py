from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    qualification = Column(String)
    department_id = Column(Integer, ForeignKey("departments.department_id"))

    department = relationship("Department", back_populates="teachers")
    courses = relationship("Course", back_populates="teacher")
