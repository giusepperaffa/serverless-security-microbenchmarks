# ---------------------
# Import Python Modules
# ---------------------
import boto3
import datetime
import json
import os
import re

# -------
# Handler
# -------
def onS3Upload(event, context):
    # ---------------------------
    # Retrieve uploaded file name
    # ---------------------------
    filesUploaded = event['Records']
    for fileUploaded in filesUploaded:
        # The following statement retrieves the filename that includes
        # the name of the folder within the S3 bucket. 
        fileName = fileUploaded["s3"]["object"]["key"]
        bucketName = fileUploaded["s3"]["bucket"]["name"]
        accountId = fileUploaded["s3"]["bucket"]["arn"].split(':')[4]
        print('--- The following file was uploaded %s ---' % fileName)
    # -----------------
    # Send notification
    # -----------------
    # Initialize boto3 client for AWS SNS service
    sns = boto3.client('sns')
    emailMsg = fileName + bucketName
    snsResponse= sns.publish(TopicArn=re.sub('\*', accountId, os.environ['TOPIC_ARN']), Message=emailMsg, Subject='Test')
    return

