from fastapi import FastAPI, status
from fastapi import HTTPException

from src.utils import Parser

app = FastAPI()

@app.get('/')
async def get_home(path: str=None):
    parser = Parser(path)
    try:
        response = await parser.parse_response()
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail='Invalid domain path')
    return response
