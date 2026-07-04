from fastapi import APIRouter

router = APIRouter()

@router.post("/{student_id}/enroll")
def enroll_student():
    return {"message": "Student enrolled in course"}

@router.delete("/{student_id}/course/{course_id}")
def unenroll_student(student_id: int, course_id: int):
    return {"message": f"Student {student_id} unenrolled from course {course_id}"}

@router.get("/{student_id}/courses")
def get_student_courses(student_id: int):
    return {"message": f"Courses for student {student_id}"}
