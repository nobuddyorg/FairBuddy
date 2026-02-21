#!/bin/bash

################
THIS SCRIPT SETS UP THE PULUMI BACKEND FOR THE FAIRBUDDY PROJECT.
IT CREATES AN S3 BUCKET TO STORE PULUMI STATE FILES AND CONFIGURES IT WITH BEST PRACTICES FOR SECURITY AND DATA PROTECTION.
THE BUCKET HAS BEEN CREATED ALREADY, THERE IS NO NEED TO RUN THIS SCRIPT AGAIN UNLESS YOU WANT TO RECREATE THE BACKEND FROM SCRATCH.
################

# create new S3 bucket for Pulumi State Files
aws s3 mb s3://fairbuddy-pulumi-state

# enable versioning for the bucket (in case of state file corruption, we can roll back to a previous version)
aws s3api put-bucket-versioning \
  --bucket fairbuddy-pulumi-state \
  --versioning-configuration Status=Enabled

# enable server-side encryption for the bucket (to protect state files at rest)
aws s3api put-bucket-encryption \
  --bucket fairbuddy-pulumi-state \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
    }]
  }'

# block public access to the bucket
aws s3api put-public-access-block \
  --bucket fairbuddy-pulumi-state \
  --public-access-block-configuration \
  BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
