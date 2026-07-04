from sqlalchemy.orm import Session
from app.repository.student_repo import student_repo
from app.schemas.student import StudentCreate, StudentUpdate
from fastapi import HTTPException

class StudentService:
    def get_student(self, db: Session, student_id: int):
        student = student_repo.get(db, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student

    def get_students(self, db: Session, skip: int = 0, limit: int = 100):
        return student_repo.get_multi(db, skip=skip, limit=limit)

    def create_student(self, db: Session, student_in: StudentCreate):
        return student_repo.create(db, obj_in=student_in)

    def update_student(self, db: Session, student_id: int, student_in: StudentUpdate):
        student = student_repo.get(db, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student_repo.update(db, db_obj=student, obj_in=student_in)

    def delete_student(self, db: Session, student_id: int):
        student = student_repo.get(db, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student_repo.remove(db, student_id=student_id)

student_service = StudentService()
