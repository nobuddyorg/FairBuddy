#!/bin/bash
# Description: Run github actions locally

pushd "$(dirname "${BASH_SOURCE[0]}")/../../" > /dev/null || exit

test -f .secrets || { echo "Error: .secrets file not found. Please create it with the necessary secrets." >&2; exit 1; }
act pull_request --secret-file .secrets

popd > /dev/null || exit
