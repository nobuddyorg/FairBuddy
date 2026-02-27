#!/usr/bin/env bash
set -euo pipefail

pushd "$(dirname "${BASH_SOURCE[0]}")/../services" > /dev/null

pkgs=()

# Populate pkgs from ../services, excluding hidden dirs and libs/
for dir in ./*/; do
  dir="${dir%/}"           # Remove trailing slash
  pkg="${dir##*/}"         # Get folder name
  [[ "$pkg" == .* || "$pkg" == "libs" ]] && continue
  pkgs+=("$pkg")
done

if [[ ${#pkgs[@]} -eq 0 ]]; then
  echo "No services found in ../services"
  popd > /dev/null
  exit 1
fi

uv sync

echo "Choose service:"
select pkg in "${pkgs[@]}"; do
  [[ -n "${pkg:-}" ]] || { echo "Invalid choice"; continue; }
  mod="${pkg//-/_}"   # Replace dashes with underscores
  exec uv run --package "$pkg" python -m "${mod}.main"
done

popd > /dev/null
