from typing import cast

import add_item.main as m
import pytest
from aws_lambda_typing.context import Context
from botocore.exceptions import ClientError


class Ctx:
    aws_request_id = "test-request-id"


def test_handler_puts_item(monkeypatch):
    calls = {}

    def put_item(**kwargs):
        calls["kwargs"] = kwargs
        return {}

    monkeypatch.setattr(
        m,
        "dynamodb",
        type("Ddb", (), {"put_item": staticmethod(put_item)})(),
    )

    res = m.handler({}, cast(Context, Ctx()))

    assert res == {"ok": True}
    assert calls["kwargs"]["TableName"] == "fairbuddy_test"
    assert calls["kwargs"]["Item"] == {
        "item": {"S": "item#2"},
        "cost": {"N": "10"},
    }


def test_handler_reraises_client_error(monkeypatch):
    def put_item(**_):
        raise ClientError(
            {"Error": {"Code": "ValidationException", "Message": "boom"}},
            "PutItem",
        )

    monkeypatch.setattr(
        m,
        "dynamodb",
        type("Ddb", (), {"put_item": staticmethod(put_item)})(),
    )

    with pytest.raises(ClientError):
        m.handler({}, cast(Context, Ctx()))
