from bs4 import BeautifulSoup
from fastapi import status

from .exceptions import ParserDataHttpException, ParserDataDomainHttpException
from .base import AbstractParser


class Parser(AbstractParser):
    @staticmethod
    async def parse(data: str = None) -> dict:
        if not data:
            raise ParserDataHttpException('Data could not be blank')

        soup = BeautifulSoup(data, 'lxml')

        no_data_status = soup.find('body').find('p')

        if no_data_status:
            raise ParserDataDomainHttpException(status_code=status.HTTP_404_NOT_FOUND, detail='There is no data about this domain')

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
