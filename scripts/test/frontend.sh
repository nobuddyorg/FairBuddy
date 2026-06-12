#!/bin/bash
# Description: Run Frontend tests

pushd "$(dirname "${BASH_SOURCE[0]}")/../../frontend" > /dev/null || exit

npm ci
npm run test

popd > /dev/null || exit
