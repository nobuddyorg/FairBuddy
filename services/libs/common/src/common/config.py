"""Configuration management for the service."""

import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Settings:
    """Immutable service configuration."""

    pulumi_outputs_file: str
    pulumi_outputs: dict = field(default_factory=dict)


def load_settings() -> Settings:
    """Load settings from environment variables and hardcoded defaults."""
    pulumi_file = ".infra-outputs.json"
    return Settings(
        pulumi_outputs_file=pulumi_file,
        pulumi_outputs=_read_pulumi_outputs(pulumi_file),
    )


def _read_pulumi_outputs(file_path: str) -> dict:
    """Read Pulumi outputs from the given JSON file."""
    json_file = Path(__file__).parent / file_path

    if not json_file.exists():
        return {}

    with json_file.open("r") as f:
        return json.load(f)
