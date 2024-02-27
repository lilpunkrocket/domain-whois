import logging
import os

from pathlib import Path


class Logger:
    def __init__(self, path: str = 'logs') -> None:
        self.path = Path(__file__).resolve().parent.parent / path
        self.logger = logging.getLogger()
        self.formatter = logging.Formatter(
            fmt='%(asctime)s - %(message)s',
        )
        if not os.path.isdir(self.path):
            os.mkdir(path=path)
        self.handler = logging.FileHandler(f'{self.path}/domain_whois.log')

        self.handler.setFormatter(self.formatter)
        self.logger.handlers = [self.handler]
        self.logger.setLevel(logging.INFO)

    async def log(self, data: dict) -> None:
        message = ''
        for value in data.values():
            message += f'{value} - '
        message = message.removesuffix('- ')
        self.logger.info(message)
