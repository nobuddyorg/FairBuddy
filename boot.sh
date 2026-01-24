#!/bin/bash

set -euo pipefail

tools=(
  awscli
  uv
)

ask() {
  local prompt="$1"
  while true; do
    read -r -p "$prompt [y/n]: " answer
    case "$answer" in
      [Yy]|[Yy][Ee][Ss]) return 0 ;;
      [Nn]|[Nn][Oo]) return 1 ;;
      *) echo "Please answer y or n." ;;
    esac
  done
}

echo "Bootstrap starting…"
echo

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
echo "Bootstrap finished."

