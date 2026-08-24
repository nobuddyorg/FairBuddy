#!/usr/bin/env bash
# Description: Run mutation testing (cosmic-ray), gate on kill rate, and emit a report + badge

set -euo pipefail

FAIL_UNDER="${1:-80}"
FAIL_OVER=$((100 - FAIL_UNDER))

pushd "$(dirname "${BASH_SOURCE[0]}")/../../" > /dev/null || exit

uv sync --dev

mkdir -p reports
session_file="reports/mutation-session.sqlite"
rm -f "$session_file"

uv run cosmic-ray init cosmic-ray.toml "$session_file"
uv run cr-filter-pragma "$session_file"
uv run cosmic-ray baseline cosmic-ray.toml
uv run cosmic-ray exec cosmic-ray.toml "$session_file"

report_output="$(uv run cr-report --surviving-only --no-show-output --no-show-diff "$session_file")"
echo "$report_output"

{
  echo "## Mutation Testing"
  echo
  echo '```'
  echo "$report_output"
  echo '```'
  echo
  echo "Minimum required kill rate: **${FAIL_UNDER}%**"
} > reports/mutation-summary.md

uv run cr-badge cosmic-ray.toml reports/mutation-badge.svg "$session_file"

uv run cr-rate "$session_file" --fail-over "$FAIL_OVER"

popd > /dev/null || exit
