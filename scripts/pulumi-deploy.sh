#!/bin/bash
# This script deploys the infrastructure using Pulumi.

pushd "../infrastructure" > /dev/null || exit

pulumi login s3://fairbuddy-pulumi-state
pulumi up

popd > /dev/null || exit
