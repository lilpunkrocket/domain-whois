from datafetcher.core import DataFetcherHttp
from parser.core import ParserHttp


class DataParser(DataFetcherHttp, ParserHttp):
    @staticmethod
    async def get_response(path: str = None, params: dict = None):
        data = await DataFetcherHttp.fetch_data(path=path, params=params)
        response = await ParserHttp.parse(data)

        return response
