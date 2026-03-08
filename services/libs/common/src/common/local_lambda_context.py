"""A mock LambdaContext for local testing."""

from aws_lambda_powertools.utilities.typing import LambdaContext


class LocalLambdaContext(LambdaContext):
    """A reusable mock LambdaContext for local testing."""

    @property
    def aws_request_id(self) -> str:
        """Return a fixed request ID for local testing."""
        return "local"

    @property
    def function_name(self) -> str:
        """Return a fixed function name for local testing."""
        return "local_function"

    @property
    def function_version(self) -> str:
        """Return a fixed function version for local testing."""
        return "$LATEST"

    @property
    def invoked_function_arn(self) -> str:
        """Return a fixed ARN for local testing."""
        return "arn:aws:lambda:local:0:function:local_function"

    @property
    def memory_limit_in_mb(self) -> int:
        """Return a fixed memory limit for local testing."""
        return 128

    @property
    def log_group_name(self) -> str:
        """Return a fixed log group name for local testing."""
        return "/aws/lambda/local_function"

    @property
    def log_stream_name(self) -> str:
        """Return a fixed log stream name for local testing."""
        return "2026/03/08/[$LATEST]localstream"


def get_context() -> LambdaContext:
    """Return an instance of LocalLambdaContext."""
    return LocalLambdaContext()
