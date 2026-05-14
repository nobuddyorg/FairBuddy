#!/bin/bash
# Description: Run integration tests

pushd "$(dirname "${BASH_SOURCE[0]}")/../../" > /dev/null || exit

uv sync
uv run pytest

popd > /dev/null || exit
