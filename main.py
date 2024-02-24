from fastapi import FastAPI, status
from fastapi import HTTPException

import os
from dotenv import load_dotenv

from utils import DataParser

app = FastAPI()
load_dotenv()

API = os.getenv('API')

@app.get('/')
async def get_home(path: str=None):
    if not path:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Try add path param to request')
    return await DataParser.get_response(path=API, params={'domain': path})
