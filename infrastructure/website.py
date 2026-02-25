"""A component that encapsulates creating an AWS S3 hosted static website."""

import pulumi
from pulumi import ResourceOptions
from pulumi_aws import s3


class AwsS3Website(pulumi.ComponentResource):
    """A component that encapsulates creating an AWS S3 hosted static website."""

    def __init__(
        self,
        name: str,
        files: list[str] | None = None,
        opts: ResourceOptions | None = None,
    ) -> None:
        """Create an AWS S3 hosted static website."""
        super().__init__("quickstart:index:AwsS3Website", name, {"files": files}, opts)

        # Create an AWS resource (S3 Bucket)
        bucket = s3.Bucket(
            "my-bucket",
            # Set the parent to the component (step #2) above.
            # Also, do the same for all other resources below.
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Turn the bucket into a website:
        website = s3.BucketWebsiteConfiguration(
            "website",
            bucket=bucket.id,
            index_document={
                "suffix": "index.html",
            },
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Permit access control configuration:
        ownership_controls = s3.BucketOwnershipControls(
            "ownership-controls",
            bucket=bucket.id,
            rule={
                "object_ownership": "ObjectWriter",
            },
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Enable public access to the website:
        public_access_block = s3.BucketPublicAccessBlock(
            "public-access-block",
            bucket=bucket.id,
            block_public_acls=False,
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Create an S3 Bucket object for each file; note the changes to name/source:
        for file in files:
            s3.BucketObject(
                file,
                bucket=bucket.id,
                source=pulumi.FileAsset(file),
                content_type="text/html",
                acl="public-read",
                opts=pulumi.ResourceOptions(
                    depends_on=[ownership_controls, public_access_block],
                    parent=self,
                ),
            )

        # Capture the URL and make it available as a component property and output:
        self.url = pulumi.Output.concat("http://", website.website_endpoint)
        self.register_outputs({"url": self.url})  # Signal component completion.
