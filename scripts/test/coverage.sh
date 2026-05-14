#!/bin/bash
# Description: Run unit tests with coverage reporting

pushd "$(dirname "${BASH_SOURCE[0]}")/../../" > /dev/null || exit

uv sync
uv run pytest \
  -m "not integration" \
  --junitxml=reports/test-results.xml \
  --cov=services \
  --cov-report=term-missing \
  --cov-report=xml:reports/coverage.xml \
  --cov-report=html:reports/htmlcov \
  --cov-fail-under=80
pytest_exit_code=$?

popd > /dev/null || exit
exit "$pytest_exit_code"
