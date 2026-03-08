"""Defines a simple Amazon DynamoDB table.

Reference:
----------
https://www.pulumi.com/docs/reference/pkg/aws/dynamodb/table/

"""

import pulumi
import pulumi_aws as aws

stack = pulumi.get_stack()

table = aws.dynamodb.Table(
    f"fairbuddy-{stack}",
    attributes=[
        aws.dynamodb.TableAttributeArgs(
            name="item",
            type="S",
        ),
    ],
    hash_key="item",
    billing_mode="PAY_PER_REQUEST",
)

table_name = table.name
