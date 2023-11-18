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
        # Create a high-level object-oriented service access
        dynamodb = boto3.resource('dynamodb')
        # Create an instance of a Table object
        table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
        # Call scan API
        result = table.scan(Select='ALL_ATTRIBUTES', ScanFilter=event['body'])
    except Exception as e:
        print('--- DynamoDB table scanning failed! ---')
        result = str(e)
        statusCode = 500
    return {'statusCode': statusCode, 'body': json.dumps({'result': result})}

