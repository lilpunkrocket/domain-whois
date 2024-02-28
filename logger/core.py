import logging
import os

from pathlib import Path


class Logger:
    def __init__(self, path: str = 'logs') -> None:
        self.path = Path(__file__).resolve().parent.parent / path

        self.info_logger = logging.getLogger('info_logger')
        self.info_logger.setLevel(logging.INFO)

        self.error_logger = logging.getLogger('error_logger')
        self.error_logger.setLevel(logging.WARNING)

        self.info_formatter = logging.Formatter(
            fmt='%(levelname)s: [%(asctime)s] - %(message)s',
        )

        self.error_formatter = logging.Formatter(
            fmt='[%(asctime)s] - %(message)s',
        )

        if not os.path.isdir(self.path):
            os.mkdir(path=path)

        self.info_handler = logging.FileHandler(f'{self.path}/access.log')
        self.info_handler.setLevel(logging.INFO)

        self.error_handler = logging.FileHandler(f'{self.path}/error.log')
        self.error_handler.setLevel(logging.WARNING)

        self.info_handler.setFormatter(self.info_formatter)
        self.error_handler.setFormatter(self.error_formatter)

        self.info_logger.handlers = [self.info_handler]
        self.error_logger.handlers = [self.error_handler]

    async def log(self, data: dict, level: str='INFO') -> None:
        message = ''
        for value in data.values():
            message += f'{value} - '
        message = message.removesuffix('- ')

        if level == 'WARNING':
            self.error_logger.warning(message)
            return
        self.info_logger.info(message)
