from abc import ABC, abstractstaticmethod


class AbstractDataFetcher(ABC):
    '''Abstract class for DataFetcher'''

    @abstractstaticmethod
    async def fetch_data(path: str = None, params: dict = None) -> str:
        '''Fetch data from path with params. Raises DataFetchException'''
