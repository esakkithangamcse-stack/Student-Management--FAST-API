from pydantic import BaseModel, EmailStr
from typing import Optional

class TeacherBase(BaseModel):
    name: str
    email: EmailStr
    qualification: Optional[str] = None
    department_id: Optional[int] = None

class TeacherCreate(TeacherBase):
    pass

class TeacherResponse(TeacherBase):
    teacher_id: int

    class Config:
        from_attributes = True
