from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.security import create_access_token, verify_password, get_password_hash

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Example logic, normally verify against DB
    if form_data.username == "admin" and form_data.password == "admin":
        access_token = create_access_token(data={"sub": form_data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")

@router.post("/register")
def register():
    return {"message": "User registered"}

@router.post("/refresh-token")
def refresh_token():
    return {"message": "Token refreshed"}

@router.post("/logout")
def logout():
    return {"message": "Logged out"}

@router.post("/forgot-password")
def forgot_password():
    return {"message": "Password reset email sent"}

@router.post("/reset-password")
def reset_password():
    return {"message": "Password reset successful"}
