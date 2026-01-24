import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Settings:
    log_level: str


def load_settings() -> Settings:
    return Settings(
        log_level=os.getenv("LOG_LEVEL", "INFO").upper(),
    )
