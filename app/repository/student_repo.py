from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate

class StudentRepository:
    def get(self, db: Session, student_id: int):
        return db.query(Student).filter(Student.student_id == student_id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Student).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: StudentCreate):
        db_obj = Student(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: Student, obj_in: StudentUpdate):
        obj_data = db_obj.__dict__
        update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, student_id: int):
        obj = db.query(Student).filter(Student.student_id == student_id).first()
        if obj:
            db.delete(obj)
            db.commit()
        return obj

student_repo = StudentRepository()
