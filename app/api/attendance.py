from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def record_attendance():
    return {"message": "Attendance recorded"}

@router.get("/student/{student_id}")
def get_student_attendance(student_id: int):
    return {"message": f"Attendance for student {student_id}"}
