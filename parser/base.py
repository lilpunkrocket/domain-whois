from abc import abstractmethod


class Parser:
    '''Abstract class for Parser'''
    
    @staticmethod
    @abstractmethod
    async def parse(data: str = None) -> dict:
        '''Parse to json by default. Raises ParserDataException'''
