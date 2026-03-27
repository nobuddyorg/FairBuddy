# test_local_lambda_context.py
from aws_lambda_powertools.utilities.typing import LambdaContext
from common.local_lambda_context import LocalLambdaContext, get_context  # adjust module

DEFAULT_MEMORY_LIMIT_MB = 128


def test_get_context_returns_local_context():
    ctx = get_context()
    assert isinstance(ctx, LambdaContext)
    assert isinstance(ctx, LocalLambdaContext)


def test_local_lambda_context_properties():
    ctx = LocalLambdaContext()
    assert ctx.aws_request_id == "local"
    assert ctx.function_name == "local_function"
    assert ctx.function_version == "$LATEST"
    assert ctx.invoked_function_arn == "arn:aws:lambda:local:0:function:local_function"
    assert ctx.memory_limit_in_mb == DEFAULT_MEMORY_LIMIT_MB
    assert ctx.log_group_name == "/aws/lambda/local_function"
    assert ctx.log_stream_name == "2026/03/08/[$LATEST]localstream"
