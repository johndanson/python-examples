###############################################################################
# Using Python to manage EC2 virtual machines on AWS
###############################################################################

import boto3
import time


# -------------------------------------------------CREATE INSTANCE
ec2 = boto3.resource('ec2')
ec2.create_instances(ImageId='ami-0ff8a91507f77f867', MinCount=1, MaxCount=1, InstanceType='t2.micro')


# -------------------------------------------------PAUSES OPERATION IN THIS CASE 250 SECONDS TO ALLOW EC2 TO INITIALIZE
time.sleep(250)

# -------------------------------------------------TERMINATE INSTANCE, (REQUIRES METADATA GET ON Inst ID.)

ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds=['i-0c26a92bb3e93d129', 'i-0188be5623dd67639']).stop()
ec2.instances.filter(InstanceIds=['i-0c26a92bb3e93d129', 'i-0188be5623dd67639']).terminate()

