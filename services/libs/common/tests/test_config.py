import dataclasses
import json
from unittest.mock import mock_open, patch

import pytest
from common.config import Settings, _read_pulumi_outputs, load_settings


def test_settings_is_immutable():
    """Settings is frozen, so attribute assignment must raise."""
    settings = Settings(pulumi_outputs_file="dummy.json")

    with pytest.raises(dataclasses.FrozenInstanceError):
        settings.pulumi_outputs_file = "other.json"  # ty: ignore[invalid-assignment]  # pyright: ignore[reportAttributeAccessIssue]


def test_settings_has_no_dict():
    """Settings uses slots, so instances must not carry a __dict__."""
    settings = Settings(pulumi_outputs_file="dummy.json")

    assert not hasattr(settings, "__dict__")


def test_read_pulumi_outputs_file_exists():
    """_read_pulumi_outputs returns dict when JSON file exists."""
    mock_data = {"stack": "test"}
    m = mock_open(read_data=json.dumps(mock_data))

    with patch("common.config.Path.open", m), patch("common.config.Path.exists", return_value=True):
        result = _read_pulumi_outputs("dummy.json")
        assert result == mock_data


def test_read_pulumi_outputs_file_missing():
    """_read_pulumi_outputs returns empty dict when file does not exist."""
    with patch("common.config.Path.exists", return_value=False):
        result = _read_pulumi_outputs("dummy.json")
        assert result == {}


def test_load_settings_reads_pulumi_outputs():
    """load_settings returns a Settings object with correct attributes."""
    mock_data = {"stack": "dev"}
    m = mock_open(read_data=json.dumps(mock_data))

    with patch("common.config.Path.open", m), patch("common.config.Path.exists", return_value=True):
        settings = load_settings()
        assert isinstance(settings, Settings)
        assert settings.pulumi_outputs_file == ".infra-outputs.json"
        assert settings.pulumi_outputs == mock_data
