#!/bin/bash
# Description: Build a production ready frontend bundle for deployment.

pushd "$(dirname "${BASH_SOURCE[0]}")/../../frontend" > /dev/null || exit

npm clean install
npm run build

popd > /dev/null || exit
