#!/bin/bash
# Description: Run integration tests

pushd "$(dirname "${BASH_SOURCE[0]}")/../../" > /dev/null || exit

if [ -z "${PULUMI_CONFIG_PASSPHRASE:-}" ]; then
  read -rsp "Enter PULUMI_CONFIG_PASSPHRASE: " PULUMI_CONFIG_PASSPHRASE
  echo
  export PULUMI_CONFIG_PASSPHRASE

  echo "Tip: exporting PULUMI_CONFIG_PASSPHRASE in your shell profile makes this easier."
fi

uv sync
pulumi login s3://fairbuddy-pulumi-state
uv run pytest

popd > /dev/null || exit
