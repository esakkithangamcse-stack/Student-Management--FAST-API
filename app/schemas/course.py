from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    course_name: str
    credits: int
    teacher_id: Optional[int] = None

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    course_id: int

    class Config:
        from_attributes = True
