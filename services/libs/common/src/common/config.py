"""Configuration management for the service."""

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Settings:
    """Immutable service configuration."""

    service: str
    log_level: str


def load_settings() -> Settings:
    """Load settings from environment variables and hardcoded defaults."""
    return Settings(
        service="fairbuddy",
        log_level=os.getenv("LOG_LEVEL", "INFO").upper(),
    )
