from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String, unique=True, index=True, nullable=False)
    hod_name = Column(String)

    students = relationship("Student", back_populates="department")
    teachers = relationship("Teacher", back_populates="department")
