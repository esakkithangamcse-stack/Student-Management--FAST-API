from fastapi import Depends, HTTPException, status
from app.api.auth import oauth2_scheme
from jose import jwt, JWTError
from app.core.config import settings

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        # In real app, fetch user from DB and return
        return {"username": username, "role": "admin"} # Mocking admin for simplicity
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

def role_required(required_role: str):
    def role_checker(current_user: dict = Depends(get_current_user)):
        if current_user.get("role") != required_role:
            raise HTTPException(status_code=403, detail="Not enough permissions")
        return current_user
    return role_checker

require_admin = role_required("admin")
require_teacher = role_required("teacher")
require_student = role_required("student")
