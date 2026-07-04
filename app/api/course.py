from fastapi import APIRouter, Depends
from typing import List
from app.schemas.course import CourseCreate, CourseResponse

router = APIRouter()

@router.post("/", response_model=CourseResponse)
def create_course(course_in: CourseCreate):
    return {"message": "Course created"}

@router.get("/", response_model=List[CourseResponse])
def read_courses():
    return []

@router.put("/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course_in: CourseCreate):
    return {"message": "Course updated"}
