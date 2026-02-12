#!/usr/bin/env bash
set -euo pipefail

BOM_FILE="bom.txt"
RUN_ALL=false

if [[ "${1:-}" == "--all" ]]; then
  RUN_ALL=true
fi

pkgs=()

while IFS= read -r line; do
  [[ -z "$line" ]] && continue
  [[ "$line" =~ ^[[:space:]]*# ]] && continue
  pkgs+=("$line")
done < "$BOM_FILE"

uv sync --group dev

if $RUN_ALL; then
  echo "Running tests for all services…"
  echo

  for pkg in "${pkgs[@]}"; do
    echo "==> Testing $pkg"
    uv run --package "$pkg" pytest -q
    echo
  done

  exit 0
fi

echo "Choose service to test:"
select pkg in "${pkgs[@]}"; do
  [[ -n "${pkg:-}" ]] || { echo "Invalid choice"; continue; }
  exec uv run --package "$pkg" pytest -q
done
