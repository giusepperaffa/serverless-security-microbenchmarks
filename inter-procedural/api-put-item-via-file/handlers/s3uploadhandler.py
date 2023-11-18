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
def updateDynamoDBTable(authorsFileFullPath, titleFileFullPath):
    dynamodbTableName = os.environ['DYNAMODB_TABLE']
    print('--- The DynamoDB table {} is about to be updated ---'.format(dynamodbTableName))
    # Create a high-level object-oriented service access
    dynamodb = boto3.resource('dynamodb')
    # Initialize the itemId by using a time stamp
    itemId = datetime.datetime.now().isoformat()
    # Create an instance of the class Table
    dynamodbTableObj = dynamodb.Table(dynamodbTableName)
    # Prepare the item to be stored in the DynamoDB table. The files
    # obtained after splitting the original one are processed to get
    # the strings to be added to the item dictionary.
    authorsInfo =  [line.split(': ')[-1] for line in open(authorsFileFullPath, mode='r')][0]
    titleInfo = [line.split(': ')[-1] for line in open(titleFileFullPath, mode='r')][0]
    # Add the new item to the DynamoDB table
    dynamodbTableObj.put_item(Item={'itemId': itemId, 'authors': authorsInfo, 'title': titleInfo})
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
    # -----------------------
    # Output files generation
    # -----------------------
    # The following code creates two different files, which contain the first
    # and the second line of the original file, respectively
    outputFileA = os.path.join('/tmp', 'outputFileA.txt')
    outputFileB = os.path.join('/tmp', 'outputFileB.txt')
    with open(downloadPath, 'r') as inputFileObj, open(outputFileA, 'w') as outputFileObjA, open(outputFileB, 'w') as outputFileObjB:
        inputFileContentsList = inputFileObj.readlines()
        # The following code assumes that the input file contains only two lines,
        # which will then be copied into two separate files.
        outputFileObjA.write(inputFileContentsList[0])
        outputFileObjB.write(inputFileContentsList[1])
    print('--- Generation of output files completed ---')
    # ---------------------
    # Update DynamoDB table
    # ---------------------
    updateDynamoDBTable(outputFileA, outputFileB)
    return

