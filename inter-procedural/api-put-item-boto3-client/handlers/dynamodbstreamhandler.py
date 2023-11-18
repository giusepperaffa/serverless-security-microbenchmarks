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
def onDynamoDBStream(event, context):
    print('--- Handler of the DynamoDB stream is being executed ---' )
    authorsInfo = event['Records'][0]['dynamodb']['NewImage']['authors']['S']
    titleInfo = event['Records'][0]['dynamodb']['NewImage']['title']['S']
    eventData = authorsInfo + titleInfo
    os.system('echo %s' % eventData)
    return

