from functools import lru_cache

from aws_lambda_powertools import Logger

from .config import load_settings


@lru_cache
def get_logger() -> Logger:
    settings = load_settings()
    return Logger(
        service=settings.service,
        level=settings.log_level,
    )
