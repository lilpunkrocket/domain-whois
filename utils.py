import aiohttp
from fastapi import status
from fastapi import HTTPException

from datafetcher.core import DataFetcher
from datafetcher.exceptions import DatafetchPathException

from parser.core import Parser
from parser.exceptions import ParserDataDomainException

class DataParser:
    @staticmethod
    async def get_response(path: str=None, params: dict=None):
        try:
            data = await DataFetcher.fetch_data(path=path, params=params)
        except DatafetchPathException:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid domain path')
        except:
            raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail='Server connection timeout')
        
        try:
            response = await Parser.parse(data)
        except ParserDataDomainException:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There is no data about this domain')
        
        return response
