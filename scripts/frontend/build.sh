#!/bin/bash
# Description: Local start of the frontend application

pushd "$(dirname "${BASH_SOURCE[0]}")/../../frontend" > /dev/null || exit

npm clean install
npm run build

popd > /dev/null || exit
