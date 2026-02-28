#!/bin/bash
# This script prints the outputs of the Pulumi stack.

pushd "$(dirname "${BASH_SOURCE[0]}")/../infrastructure" > /dev/null || exit

pulumi login s3://fairbuddy-pulumi-state
pulumi stack output

popd > /dev/null || exit
