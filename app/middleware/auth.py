from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.security import settings
from jose import jwt, JWTError

class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Allow open routes
        if request.url.path in ["/docs", "/openapi.json", "/auth/login", "/auth/register"]:
            return await call_next(request)
        
        # We can implement token verification here or use FastAPI Depends
        # Depends is better for role based routing. Let's pass for now and rely on Depends
        return await call_next(request)
