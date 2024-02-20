import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

class Parser:
    def __init__(self, path: str = '') -> None:
        self.__path = path
        self.__api = os.getenv('API')

    async def get_response(self, path: str = None):
        if not path and self.__path == '':
            raise ValueError


        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.__api}?domain={path}') as resp:
                return await resp.text()

    async def parse_response(self, response: str = None):
        if not response:
            response = await self.get_response(self.__path)

        soup = BeautifulSoup(response, 'lxml')
        await self.check_bad_response(soup=soup)
        all_table_rows = soup.find('table').find_all('tr')
        result_dict = dict()
        current_dict_key = 'common info'
        for row in all_table_rows:
            all_row_dats = row.find_all('td')

            if len(all_row_dats) == 1:
                current_dict_key = all_row_dats[0].text
                continue

            result_dict[current_dict_key] = {**result_dict.get(current_dict_key, {}),
                                             **{all_row_dats[0].text: all_row_dats[1].text}}

        return result_dict
    
    async def check_bad_response(self, soup: BeautifulSoup):
        status = soup.find('body').find('p')
        if status:
            raise ValueError(f'{status.text}')
        
