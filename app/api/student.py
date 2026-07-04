from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, UploadFile, File
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.session import get_db
from app.schemas.student import StudentCreate, StudentUpdate, StudentResponse
from app.services.student_service import student_service

router = APIRouter()

def send_welcome_email(email: str):
    print(f"Sending welcome email to {email}")

@router.post("/", response_model=StudentResponse)
def create_student(
    student_in: StudentCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    student = student_service.create_student(db, student_in)
    background_tasks.add_task(send_welcome_email, student.email)
    return student

@router.get("/", response_model=List[StudentResponse])
def read_students(
    page: int = 1,
    limit: int = 20,
    search: Optional[str] = None,
    department: Optional[str] = None,
    gender: Optional[str] = None,
    sort_by: Optional[str] = "name",
    sort_order: Optional[str] = "asc",
    db: Session = Depends(get_db)
):
    skip = (page - 1) * limit
    # In a real app, pass all these parameters to the repository
    return student_service.get_students(db, skip=skip, limit=limit)

@router.get("/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    return student_service.get_student(db, student_id)

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student_in: StudentUpdate, db: Session = Depends(get_db)):
    return student_service.update_student(db, student_id, student_in)

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student_service.delete_student(db, student_id)
    return {"message": "Student deleted successfully"}

@router.post("/{student_id}/photo")
async def upload_student_photo(student_id: int, file: UploadFile = File(...)):
    # Simulating file upload
    return {"filename": file.filename, "student_id": student_id}


def generate_report_task(student_id: int):
    print(f"Generating report for student {student_id}")

@router.post("/{student_id}/report")
def generate_report(student_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(generate_report_task, student_id)
    return {"message": "Report generation started in background"}
