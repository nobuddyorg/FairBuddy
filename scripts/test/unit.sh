#!/bin/bash
# Description: Run unit tests

pushd "$(dirname "${BASH_SOURCE[0]}")/../../" > /dev/null || exit

uv sync
uv run pytest -m "not integration"

popd > /dev/null || exit
