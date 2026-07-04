from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def add_marks():
    return {"message": "Marks added"}

@router.get("/student/{student_id}")
def get_student_marks(student_id: int):
    return {"message": f"Marks for student {student_id}"}
