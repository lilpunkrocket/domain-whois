from abc import abstractmethod


class DataFetcher:
    '''Abstract class for DataFetcher'''

    @staticmethod
    @abstractmethod
    async def fetch_data(path: str = None, params: dict = None) -> str:
        '''Fetch data from path with params. Raises DataFetchException'''
