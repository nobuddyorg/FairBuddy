from unittest.mock import patch

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
