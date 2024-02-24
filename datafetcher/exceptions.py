from fastapi import HTTPException


class DatafetchPathException(Exception):
    '''Invalid path exception'''


class DatafetchServerTimeoutException(Exception):
    '''Request to server timeout'''


class DatafetchPathHttpException(DatafetchPathException, HTTPException):
    '''Invalid path exception'''


class DatafetchServerTimeoutHttpException(DatafetchServerTimeoutException, HTTPException):
    '''Request to server timeout'''
