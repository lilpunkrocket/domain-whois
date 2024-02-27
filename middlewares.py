from fastapi import Request
from logger.core import Logger
from starlette.middleware.base import BaseHTTPMiddleware

logger = Logger()
class LogMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        response = await call_next(request)

        log_dict = {
            'client': request.client.host,
            'method': request.method,
            'url': request.url,
            'response_status_code': response.status_code,
        }

        await logger.log(log_dict)

        return response