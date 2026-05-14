#!/bin/bash
# Description: Run github actions locally

pushd "$(dirname "${BASH_SOURCE[0]}")/../../" > /dev/null || exit

act pull_request --secret-file .secrets

popd > /dev/null || exit
