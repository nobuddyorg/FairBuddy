"""AWS Lambda function to add an item to a DynamoDB table."""

from typing import Any, cast

import boto3
from aws_lambda_typing.context import Context
from common.config import load_settings
from common.logging import get_logger

logger = get_logger()
settings = load_settings()

dynamodb = boto3.client("dynamodb")


def handler(event: dict[str, Any], context: Context) -> dict[str, object]:
    """Handle an AWS Lambda request to add an item to the DynamoDB table."""
    logger.info("start request_id=%s", getattr(context, "aws_request_id", "-"))
    logger.info("log_level=%s", settings.log_level)
    logger.info("event=%s", event)

    try:
        resp = dynamodb.put_item(
            TableName="fairbuddy_test",
            Item={
                "item": {"S": "item#2"},
                "cost": {"N": "10"},
            },
        )
    except Exception:
        logger.exception("put_item failed")
        raise
    else:
        logger.info(
            "put_item ok consumed_capacity=%s",
            resp.get("ConsumedCapacity"),
        )
        return {"ok": True}


def main() -> dict[str, object]:
    """Run the handler locally (not used by AWS Lambda, but can be triggered with trigger.sh)."""

    class _LocalContext:
        aws_request_id = "local"

    return handler({}, cast("Context", _LocalContext()))


if __name__ == "__main__":
    main()
