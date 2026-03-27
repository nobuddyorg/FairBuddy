from unittest.mock import patch

import add_item.main as main_module
from add_item.main import get_context, lambda_handler


@patch("add_item.main.load_settings")
def test_lambda_handler_returns_success_message(mock_load_settings):
    # given
    mock_load_settings.return_value.pulumi_outputs = {"table_name": "test-table"}
    context = get_context()

    # when
    result = lambda_handler({"key": "value"}, context)

    # then
    assert result == "Item added successfully!"
    mock_load_settings.assert_called_once()


def test_main_calls_lambda_handler():
    with patch("add_item.main.lambda_handler") as mock_handler, patch("add_item.main.get_context") as mock_context:
        mock_handler.return_value = "mocked result"
        mock_context.return_value = "mocked context"

        result = main_module.main()

        mock_handler.assert_called_once_with({}, "mocked context")
        assert result == "mocked result"
