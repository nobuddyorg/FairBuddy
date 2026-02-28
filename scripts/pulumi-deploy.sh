#!/bin/bash
# This script deploys the infrastructure using Pulumi.

pushd "$(dirname "${BASH_SOURCE[0]}")/../infrastructure" > /dev/null || exit

pulumi login s3://fairbuddy-pulumi-state
pulumi up

popd > /dev/null || exit
