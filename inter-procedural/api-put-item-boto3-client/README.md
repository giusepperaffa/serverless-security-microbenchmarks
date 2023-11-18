# Description
Microbenchmark containing three handlers, i.e., `onHTTPPostEvent`, `onS3Upload` and `onDynamoDBStream`. The first is triggered by a HTTP request, the second is executed as a consequence of an event raised by the API `upload_file`, whereas the third is triggered by the API `put_item` used to create a new item in a DynamoDB Table. Note that:

* The expected data flow goes through the helper function `updateDynamoDBTable`, which is _not_ an event-triggered handler.
* The `boto3` interface object for DynamoDB is an instance of `boto3.client`.

# Expected Results
The analysis tool is expected to identify the following data flows:

* Source: `event` input argument in the definition of the handler `onHTTPPostEvent`, i.e., `def onHTTPPostEvent(event, context):`
* Sink: `os.system('echo %s' % eventData)` (handler `onDynamoDBStream`)
