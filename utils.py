from datafetcher.core import DataFetcher
from parser.core import Parser


class DataParser(DataFetcher, Parser):
    @staticmethod
    async def get_response(self, path: str = None, params: dict = None):
        data = await self.fetch_data(path=path, params=params)
        response = await self.parse(data)

        return response
