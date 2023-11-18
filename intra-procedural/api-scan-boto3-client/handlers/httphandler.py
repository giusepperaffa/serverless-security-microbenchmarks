# ---------------------
# Import Python Modules
# ---------------------
import boto3
import json
import os

# -------
# Handler 
# -------
def onHTTPPostEvent(event, context):
    # Default value for statusCode
    statusCode = 200
    # If no body is found, a default result is returned
    if not event.get('body'):
        return {'statusCode': 400, 'body': json.dumps({'result': 'No body was found'})}
    # Scan DynamoDB table
    try:
        # Create an instance of the client object for DynamoDB
        dynamodb = boto3.client('dynamodb')
        # Call scan API
        result = dynamodb.scan(TableName=os.environ['DYNAMODB_TABLE'], Select='ALL_ATTRIBUTES', ScanFilter=event['body'])
    except Exception as e:
        print('--- DynamoDB table scanning failed! ---')
        result = str(e)
        statusCode = 500
    return {'statusCode': statusCode, 'body': json.dumps({'result': result})}

