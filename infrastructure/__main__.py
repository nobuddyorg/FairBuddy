"""A Pulumi program that creates an AWS S3 hosted static website using a component."""

import pulumi

# Import from our new component module:
from website import AwsS3Website

# Create an instance of our component with the same files as before:
website = AwsS3Website("my-website", files=["index.html"])

# And export its autoassigned URL:
pulumi.export("url", website.url)
