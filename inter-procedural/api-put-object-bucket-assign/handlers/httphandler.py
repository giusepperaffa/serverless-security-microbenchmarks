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
    # Create a high-level object-oriented service access
    s3_resource = boto3.resource('s3')
    s3_bucket = s3_resource.Bucket(os.environ['BUCKET_NAME'])
    s3_bucket.put_object(Key=s3BucketKey)
    return

