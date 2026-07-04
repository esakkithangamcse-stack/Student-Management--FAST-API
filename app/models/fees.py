from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Fees(Base):
    __tablename__ = "fees"

    fee_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False) # Paid, Pending
    payment_date = Column(Date)

    student = relationship("Student", back_populates="fees")
