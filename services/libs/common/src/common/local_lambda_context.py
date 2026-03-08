# ruff: noqa: D101, D102

"""A mock LambdaContext for local testing."""

from aws_lambda_powertools.utilities.typing import LambdaContext


class LocalLambdaContext(LambdaContext):
    @property
    def aws_request_id(self) -> str:
        return "local"

    @property
    def function_name(self) -> str:
        return "local_function"

    @property
    def function_version(self) -> str:
        return "$LATEST"

    @property
    def invoked_function_arn(self) -> str:
        return "arn:aws:lambda:local:0:function:local_function"

    @property
    def memory_limit_in_mb(self) -> int:
        return 128

    @property
    def log_group_name(self) -> str:
        return "/aws/lambda/local_function"

    @property
    def log_stream_name(self) -> str:
        return "2026/03/08/[$LATEST]localstream"


def get_context() -> LambdaContext:
    """Return an instance of LocalLambdaContext."""
    return LocalLambdaContext()
