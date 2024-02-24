from abc import ABC, abstractstaticmethod

class AbstractParser(ABC):
    '''Abstract class for Parser'''
    
    @abstractstaticmethod
    async def parse(data: str = None) -> dict:
        '''Parse to json by default. Raises ParserDataException'''
