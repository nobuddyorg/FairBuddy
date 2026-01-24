from aws_lambda_powertools import Logger
from .config import load_settings

_logger = None


def get_logger():
    global _logger
    if _logger is None:
        settings = load_settings()
        _logger = Logger(
            service=settings.service,
            level=settings.log_level,
        )
    return _logger
