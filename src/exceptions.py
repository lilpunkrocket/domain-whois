from fastapi.responses import PlainTextResponse
from logger.core import Logger

logger = Logger()


async def http_exception_handler(request, exc):
    log_dict = {
        'client': request.client.host,
        'method': request.method,
        'url': request.url,
        'response_status_code': exc.status_code,
        'data': str(exc.detail),
    }
    await logger.log(log_dict, 'WARNING')

    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
