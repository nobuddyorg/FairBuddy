"""AWS Lambda function to add an item to a DynamoDB table."""

import boto3
from aws_lambda_powertools import Logger
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from common.config import load_settings
from common.local_lambda_context import get_context

logger = Logger()

dynamodb = boto3.client("dynamodb")


@logger.inject_lambda_context(correlation_id_path=correlation_paths.LAMBDA_FUNCTION_URL)
def lambda_handler(event: dict, context: LambdaContext) -> str:
    """Handle an AWS Lambda request to add an item to the DynamoDB table."""
    logger.info("start request_id=%s", getattr(context, "aws_request_id", "-"))
    logger.info("event=%s", event)

    logger.info("Using table: %s", load_settings().pulumi_outputs.get("table_name"))
    return "Item added successfully!"


def main() -> str:
    """Run the handler locally (not used by AWS Lambda, but can be triggered with trigger.sh)."""
    return lambda_handler({}, get_context())


if __name__ == "__main__":
    main()
