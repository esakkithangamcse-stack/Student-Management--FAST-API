import time
import logging
import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        logger.info(f"Request {request_id} started: {request.method} {request.url}")
        start_time = time.time()
        
        response = await call_next(request)
        
        process_time = time.time() - start_time
        logger.info(f"Request {request_id} completed in {process_time:.4f}s with status {response.status_code}")
        response.headers["X-Process-Time"] = str(process_time)
        response.headers["X-Request-ID"] = request_id
        
        return response
