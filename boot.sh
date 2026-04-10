#!/bin/bash

# Exit immediately on error (-e),
# treat unset variables as errors (-u),
# and fail pipelines if any command fails (-o pipefail)
set -euo pipefail

# Ask a yes/no question in a loop until valid input is provided
# Returns 0 (true) for yes, 1 (false) for no
ask() {
  local prompt="$1"
  while true; do
    read -r -p "$prompt [y/n]: " answer
    case "$answer" in
      [Yy]|[Yy][Ee][Ss]) return 0 ;;      # User answered yes
      [Nn]|[Nn][Oo]) return 1 ;;          # User answered no
      *) echo "Please answer y or n." ;;  # Invalid input, retry
    esac
  done
}

echo "Bootstrap starting…"

# Define the steps as a JSON array of objects, each with a question and a command
steps=(
  "Install Homebrew?|/bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
  "Install/Upgrade homebrew tools?|brew bundle check || brew bundle install"
  "Install opengrep static code analysis?|curl -fsSL https://raw.githubusercontent.com/opengrep/opengrep/main/install.sh -o /tmp/install.sh && bash /tmp/install.sh"
  "Install pinned Python version with uv?|uv python install"
  "Install project dependencies?|uv sync"
  "Run aws configure now?|uv run aws configure"
  "Install pre-commit hooks?|uv run prek install && uv run prek install --hook-type commit-msg"
)

for step in "${steps[@]}"; do
  IFS='|' read -r question command <<< "$step"

  echo
  if ask "$question"; then
    bash -c "$command"
  fi
done

echo
echo "Bootstrap finished."
