# Description
Microbenchmark identical to [api-scan-boto3-client](../api-scan-boto3-client), except for:

* The `boto3` interface object for DynamoDB is an instance of `boto3.resource`, which is used to initialize an object of type `Table`.
* The `scan` API is called on the `Table` object.

To identify the expected data flow, a Pysa model for the `Table` API `scan` has to be used.

# Expected Results
The analysis tool is expected to identify the following data flows:

* Source: `event` input argument in the definition of the handler `onHTTPPostEvent`, i.e., `def onHTTPPostEvent(event, context):`
* Sink: `ScanFilter=event['body']` (input argument of the `scan` API call in the handler `onHTTPPostEvent`)
