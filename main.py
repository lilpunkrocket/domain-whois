from fastapi import FastAPI

from src.utils import Parser

app = FastAPI()

@app.get('/')
async def get_home(path: str=None):
    parser = Parser(path)
    try:
        response = await parser.parse_response()
    except ValueError:
        response = {'error': 'Invalid domain path'}
    return response
