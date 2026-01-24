import boto3
from common.config import load_settings
from common.logging import get_logger

logger = get_logger()
settings = load_settings()

dynamodb = boto3.client("dynamodb")


def handler(event, context):
    logger.info("start request_id=%s", getattr(context, "aws_request_id", "-"))
    logger.info("log_level=%s", settings.log_level)

    try:
        resp = dynamodb.put_item(
            TableName="fairbuddy_test",
            Item={
                "item": {"S": "item#2"},
                "cost": {"N": "10"},
            },
        )

        logger.info(
            "put_item ok consumed_capacity=%s",
            resp.get("ConsumedCapacity"),
        )

        return {"ok": True}
    except Exception:
        logger.exception("put_item failed")
        raise


def main():
    class _LocalContext:
        aws_request_id = "local"

    return handler({}, _LocalContext())


if __name__ == "__main__":
    main()
