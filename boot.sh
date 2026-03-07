#!/bin/bash

# Exit immediately on error (-e),
# treat unset variables as errors (-u),
# and fail pipelines if any command fails (-o pipefail)
set -euo pipefail

# List of tools that can optionally be installed via Homebrew
############
tools=(
  awscli
  uv
  prek
  pulumi/tap/pulumi
)
############

# Ask a yes/no question in a loop until valid input is provided
# Returns 0 (true) for yes, 1 (false) for no
ask() {
  local prompt="$1"
  while true; do
    read -r -p "$prompt [y/n]: " answer
    case "$answer" in
      [Yy]|[Yy][Ee][Ss]) return 0 ;;  # User answered yes
      [Nn]|[Nn][Oo]) return 1 ;;      # User answered no
      *) echo "Please answer y or n." ;;  # Invalid input, retry
    esac
  done
}

echo "Bootstrap starting…"
echo

# Iterate over each tool and optionally install it
for tool in "${tools[@]}"; do
  if ask "Install $tool?"; then
    brew install "$tool" || true
  fi
  echo
done

if ask "Run aws configure now?"; then
  aws configure
fi

echo
if ask "Install pre-commit hooks?"; then
  prek install
  prek install --hook-type commit-msg
fi

echo
if ask "Install project dependencies?"; then
  uv sync
fi

echo
echo "Bootstrap finished."
