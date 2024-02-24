import aiohttp
from aiohttp import ClientTimeout

from .exceptions import DatafetchPathException

class DataFetcher:
    @staticmethod
    async def fetch_data(path: str = None, params: dict = None) -> str:
        if not path:
            raise DatafetchPathException('Path could not be blank')

        async with aiohttp.ClientSession(timeout=ClientTimeout(total=15)) as session:
            async with session.get(path, params=params if params else None) as resp:
                return await resp.text()
    