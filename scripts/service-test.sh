#!/usr/bin/env bash
set -euo pipefail

pushd "$(dirname "${BASH_SOURCE[0]}")/../services" > /dev/null

RUN_ALL=false

if [[ "${1:-}" == "--all" ]]; then
  RUN_ALL=true
fi

pkgs=()

# Populate pkgs from ../services, excluding hidden dirs and libs/
for dir in ./*/; do
  dir="${dir%/}"
  pkg="${dir##*/}"
  [[ "$pkg" == .* || "$pkg" == "libs" ]] && continue
  pkgs+=("$pkg")
done

uv sync --group dev

if $RUN_ALL; then
  echo "Running tests for all services…"
  echo

  for pkg in "${pkgs[@]}"; do
    echo "==> Testing $pkg"
    uv run --package "$pkg" pytest -q
    echo
  done

  popd > /dev/null
  exit 0
fi

echo "Choose service to test:"
select pkg in "${pkgs[@]}"; do
  [[ -n "${pkg:-}" ]] || { echo "Invalid choice"; continue; }
  exec uv run --package "$pkg" pytest -q
done

popd > /dev/null
