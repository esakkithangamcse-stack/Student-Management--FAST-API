from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def add_fee():
    return {"message": "Fee added"}

@router.get("/student/{student_id}")
def get_student_fees(student_id: int):
    return {"message": f"Fees for student {student_id}"}
