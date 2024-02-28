from src.exceptions import http_exception_handler
from src.utils import DataParser
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import FastAPI, status
from fastapi import HTTPException
import os
from dotenv import load_dotenv
from src.middlewares import LogMiddleWare


app = FastAPI()
app.add_middleware(LogMiddleWare)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)

load_dotenv()

API = os.getenv('API')


@app.get('/')
async def get_home(path: str = None):
    if not path:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Try add path param to request')
    return await DataParser.get_response(DataParser, path=API, params={'domain': path})
