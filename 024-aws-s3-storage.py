###############################################################################
# S3 Storage
###############################################################################


# generate an access key and a secret key from the AWS console

# Access key ID (Fake)	            AKIAJIID2XTPZNFJV35Q

# Secret access key (Fake)          AuMD5Omsc4ypy0GbOKizbgiiMuSmNnDvk1y9BLyr

# get aws cli here                  https://aws.amazon.com/cli/.

# install aws cli

# install boto3 c:\users using pip install boto3 (run as admin)

# use aws cli here; C:\Program Files\Amazon\AWSCLI

# type aws configure

# enter secret key id and secret access key

# enter region - such as us-east-1

# enter output format text(tab-delimited), json or table'

# Import boto3 to run silently, create a resource and name the bucket.

# Each bucket name is unique, so appending datetime data or other codes will guarantee creation.

# For regions outside of east-1 append     , CreateBucketConfiguration={'LocationConstraint': 'region-code-no'})


import boto3    # library connects local CLI to AWS with Python

# Creates and deletes buckets, puts objects, prints bucket names and so on....

import time     # time pause library

s3 = boto3.resource('s3')
counter = 0
while counter < 4:
    counter = counter + 1

    x = "bucket-created-00" + str(counter)
    y = "c:\python\profile" + str(counter) + ".txt"
    print(x)

# -------------------------------------------------CREATE BUCKETS
    s3.create_bucket(Bucket=x)

# -------------------------------------------------PUT RELATED FILE IN BUCKET
    s3.Object(x, y).put(Body=open(y, 'rb'))

# -------------------------------------------------PAUSES OPERATION IN THIS CASE 25 SECONDS
time.sleep(25)

# -------------------------------------------------DELETE BUCKET OBJECTS, AND BUCKET

counter2 = 0
while counter2 < 4:
    counter2 = counter2 + 1
    x = "bucket-created-00" + str(counter2)
    y = "c:\python\profile" + str(counter2) + ".txt"
    print("deleting... " + x)

    bucket = s3.Bucket(x)

    for object in bucket.objects.all():
        object.delete()
    bucket.delete()

# ------------------------------------------------PRINT ALL BUCKET NAMES
# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
# print(bucket.name)



