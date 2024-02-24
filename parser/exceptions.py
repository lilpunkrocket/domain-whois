from fastapi import HTTPException


class ParserDataException(Exception):
    '''Invalid data to parse'''


class ParserDataDomainException(Exception):
    '''There is no data for this domain'''


class ParserDataHttpException(ParserDataException, HTTPException):
    '''Invalid data to parse'''


class ParserDataDomainHttpException(ParserDataDomainException, HTTPException):
    '''There is no data for this domain'''
