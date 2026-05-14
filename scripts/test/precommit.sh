#!/bin/bash
# Description: Run all pre-commit hooks

pushd "$(dirname "${BASH_SOURCE[0]}")/../../" > /dev/null || exit

uv run prek run --all-files

popd > /dev/null || exit
