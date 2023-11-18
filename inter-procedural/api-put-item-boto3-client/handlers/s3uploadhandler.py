# ---------------------
# Import Python Modules
# ---------------------
import boto3
import datetime
import json
import os

# ---------------
# Helper Function
# ---------------
def updateDynamoDBTable(authorsString, titleString):
    dynamodbTableName = os.environ['DYNAMODB_TABLE']
    print('--- The DynamoDB table {} is about to be updated ---'.format(dynamodbTableName))
    # Create an instance of the client object for DynamoDB
    dynamodb = boto3.client('dynamodb')
    # Initialize the itemId by using a time stamp
    itemId = datetime.datetime.now().isoformat()
    # Prepare the item to be stored in the DynamoDB table. The input
    # strings are processed to obtain those to be added to the item 
    # dictionary.
    authorsInfo =  authorsString.split(': ')[-1]
    titleInfo = titleString.split(': ')[-1]
    # Add the new item to the DynamoDB table
    dynamodb.put_item(Item={'itemId': {'S': itemId}, 'authors': {'S': authorsInfo}, 'title': {'S': titleInfo}},
        TableName=dynamodbTableName)
    print('--- The DynamoDB table {} has been updated ---'.format(dynamodbTableName))

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
        print('--- The following file was uploaded %s ---' % fileName)
    # ----------------------
    # Download uploaded file
    # ----------------------
    # Create a high-level object-oriented service access
    s3 = boto3.resource('s3')
    # Download the file existing in the bucket
    downloadPath = os.path.join('/tmp', os.path.split(fileName)[-1])  
    s3.Object(bucketName, fileName).download_file(downloadPath)
    print(f'--- Download from bucket {bucketName} completed ---')
    # --------------------
    # Read downloaded file
    # --------------------
    with open(downloadPath, 'r') as inputFileObj:
        inputFileContentsList = inputFileObj.readlines()
    # ---------------------
    # Update DynamoDB table
    # ---------------------
    updateDynamoDBTable(inputFileContentsList[0], inputFileContentsList[1])
    return

