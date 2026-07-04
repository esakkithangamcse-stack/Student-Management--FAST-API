from fastapi import FastAPI
from app.db.database import engine, Base
from app.api import student, teacher, course, auth, attendance, marks, fees, enrollment
from app.middleware.logging import LoggingMiddleware

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="A complete end-to-end FastAPI project for student management",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add Middlewares
app.add_middleware(LoggingMiddleware)

# Include Routers
app.include_router(student.router, prefix="/students", tags=["students"])
app.include_router(teacher.router, prefix="/teachers", tags=["teachers"])
app.include_router(course.router, prefix="/courses", tags=["courses"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(attendance.router, prefix="/attendance", tags=["attendance"])
app.include_router(marks.router, prefix="/marks", tags=["marks"])
app.include_router(fees.router, prefix="/fees", tags=["fees"])
app.include_router(enrollment.router, prefix="/students", tags=["enrollment"])


@app.get("/")
def root():
    return {"message": "Welcome to Student Management API"}
