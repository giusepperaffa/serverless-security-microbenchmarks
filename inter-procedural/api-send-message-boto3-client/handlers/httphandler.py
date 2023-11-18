# ---------------------
# Import Python Modules
# ---------------------
import boto3
import json
import os 

# --------------------
# SQS Producer Handler
# --------------------
def onHTTPPostEvent(event, context):
    print('--- SQS producer handler being executed ---')
    # Initialization of the strings used in the returned message
    statusCode = 200
    message = ''
    # If no body is found, a default message is returned
    if not event.get('body'):
        return {'statusCode': 400, 'body': json.dumps({'message': 'No body was found'})}
    # Send a message to the SQS queue
    try:
        # SQS client initialization
        sqs = boto3.client('sqs')
        sqs.send_message(QueueUrl=os.getenv('QUEUE_URL'), MessageBody=event['body'])
        message = 'Message accepted!'
    except Exception as e:
        print('--- Sending message to SQS queue failed! ---')
        message = str(e)
        statusCode = 500
    return {'statusCode': statusCode, 'body': json.dumps({'message': message})}

# --------------------
# SQS Consumer Handler
# --------------------
def onSQSMessage(event, context):
    print('--- SQS consumer handler being executed ---')
    # ---------------------
    # Retrieve message body
    # ---------------------
    for record in event['Records']:
        # Message deserialization. The retrieved JSON string is mapped into a dictionary
        msgBodyDict = json.loads(record["body"])
    # -----------------
    # Set S3 bucket key
    # -----------------
    # Folder within the bucket and name of the uploaded file
    uploadFileFolder = 'uploads'
    uploadFileName = msgBodyDict + '.txt'
    s3BucketKey = os.path.join(uploadFileFolder, uploadFileName)
    # --------------------------------------------------------
    # Set local path (where the file to be uploaded is stored)
    # --------------------------------------------------------
    localFile = os.path.join('/tmp', uploadFileName)
    # --------------------
    # Call upload_file API
    # --------------------
    # Create a boto3 client object instance
    s3_client = boto3.client('s3')
    s3_client.upload_file(localFile, os.environ['BUCKET_NAME'], s3BucketKey)
    return

