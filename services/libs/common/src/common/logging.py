import os

from aws_lambda_powertools import Logger

_logger = Logger(service="fairbuddy", level=os.getenv("LOG_LEVEL", "INFO").upper())


def get_logger():
    return _logger
