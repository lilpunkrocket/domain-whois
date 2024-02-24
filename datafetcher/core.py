import aiohttp

from fastapi import status
from aiohttp import ClientTimeout

from .exceptions import DatafetchPathHttpException, DatafetchServerTimeoutHttpException
from .base import DataFetcher

class DataFetcherHttp(DataFetcher):
    @staticmethod
    async def fetch_data(path: str = None, params: dict = None) -> str:
        if not path:
            raise DatafetchPathHttpException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid domain path')

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(path, params=params if params else None, timeout=ClientTimeout(total=15)) as resp:
                    return await resp.text()
            except:
                raise DatafetchServerTimeoutHttpException(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail='Server connection timeout')
    