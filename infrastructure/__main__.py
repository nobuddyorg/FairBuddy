"""The pulumi entrypoint. All infrastructure components are imported and used here."""

import pulumi
from dynamodb import table_name

pulumi.export("table_name", table_name)
