#!/bin/bash
# This script destroys the infrastructure using Pulumi.

pushd "$(dirname "${BASH_SOURCE[0]}")/../infrastructure" > /dev/null || exit

pulumi login s3://fairbuddy-pulumi-state
pulumi destroy

popd > /dev/null || exit
