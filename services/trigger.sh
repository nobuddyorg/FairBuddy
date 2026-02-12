#!/usr/bin/env bash
set -euo pipefail

BOM_FILE="bom.txt"

pkgs=()

while IFS= read -r line; do
  [[ -z "$line" ]] && continue
  [[ "$line" =~ ^[[:space:]]*# ]] && continue
  pkgs+=("$line")
done < "$BOM_FILE"

if [[ ${#pkgs[@]} -eq 0 ]]; then
  echo "No packages found in $BOM_FILE"
  exit 1
fi

uv sync

echo "Choose service:"
select pkg in "${pkgs[@]}"; do
  [[ -n "${pkg:-}" ]] || { echo "Invalid choice"; continue; }
  mod="${pkg//-/_}"
  exec uv run --package "$pkg" python -m "${mod}.main"
done
