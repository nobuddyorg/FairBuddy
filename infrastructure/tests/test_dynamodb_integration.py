# ruff: noqa: PLC0415

import os
import uuid

import boto3
import pytest
from pulumi import automation as auto

PROJECT_NAME = "fairbuddy-infra"
STACK_NAME = f"test-{uuid.uuid4().hex[:8]}"


@pytest.fixture(scope="module")
def aws_region():
    return os.getenv("AWS_REGION", "eu-central-1")


@pytest.fixture(scope="module")
def dynamodb_client(aws_region):
    return boto3.client("dynamodb", region_name=aws_region)


@pytest.mark.integration
def test_deploy_and_table_access(dynamodb_client, aws_region):
    """Deploy using Automation API, check the DynamoDB table exists, and test access."""

    # Pulumi program defining the table
    def pulumi_program():
        from pulumi import export

        from infrastructure.dynamodb import table  # creates the resource

        export("table_name", table.name)

    # Create/select the stack
    stack = auto.create_or_select_stack(
        stack_name=STACK_NAME,
        project_name=PROJECT_NAME,
        program=pulumi_program,
    )

    # Set AWS region
    stack.set_config("aws:region", auto.ConfigValue(value=aws_region))

    # Deploy the stack
    up_res = stack.up(on_output=print)
    table_name = up_res.outputs["table_name"].value
    assert table_name, "table_name output should be present"

    # --- DynamoDB access test ---
    # Generate a unique test ID
    test_id = str(uuid.uuid4())
    test_item = {"item": {"S": test_id}, "value": {"S": "hello"}}

    # Put the item
    dynamodb_client.put_item(TableName=table_name, Item=test_item)

    # Get the item back
    response = dynamodb_client.get_item(TableName=table_name, Key={"item": {"S": test_id}})
    assert "Item" in response
    assert response["Item"]["value"]["S"] == "hello"

    # Clean up the test item
    dynamodb_client.delete_item(TableName=table_name, Key={"item": {"S": test_id}})

    # --- End DynamoDB access test ---

    # Clean up Pulumi stack
    stack.destroy(on_output=print)
    stack.workspace.remove_stack(STACK_NAME)
