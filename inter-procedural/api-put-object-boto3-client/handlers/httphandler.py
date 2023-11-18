# ---------------------
# Import Python Modules
# ---------------------
import boto3
import os 

# -------
# Handler 
# -------
def onHTTPPostEvent(event, context):
    # ---------------------
    # Retrieve message body
    # ---------------------
    msgBodyDict = event['body']
    # -----------------
    # Set S3 bucket key
    # -----------------
    # Folder within the bucket and name of the uploaded file
    uploadFileFolder = 'uploads'
    uploadFileName = msgBodyDict + '.txt'
    s3BucketKey = os.path.join(uploadFileFolder, uploadFileName)
    # -------------------
    # Call put_object API
    # -------------------
    # Create a boto3 client object instance
    s3_client = boto3.client('s3')
    s3_client.put_object(Bucket=os.environ['BUCKET_NAME'], Key=s3BucketKey)
    return

