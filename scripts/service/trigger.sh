#!/usr/bin/env bash
# Description: Manual trigger for a lambda function/service.

set -euo pipefail

# Creates a json file with the outputs of the Pulumi stack, which can be read by the services to get infrastructure details like table names, API endpoints, etc.
pushd "$(dirname "${BASH_SOURCE[0]}")/../../infrastructure" > /dev/null || exit
  pulumi stack output --json > ../services/libs/common/src/common/.infra-outputs.json
popd > /dev/null || exit


pushd "$(dirname "${BASH_SOURCE[0]}")/../services" > /dev/null || exit

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
  popd > /dev/null || exit
  exit 1
fi

uv sync

echo "Choose service:"
select pkg in "${pkgs[@]}"; do
  [[ -n "${pkg:-}" ]] || { echo "Invalid choice"; continue; }
  mod="${pkg//-/_}"   # Replace dashes with underscores
  exec uv run --package "$pkg" python -m "${mod}.main"
done

popd > /dev/null || exit
