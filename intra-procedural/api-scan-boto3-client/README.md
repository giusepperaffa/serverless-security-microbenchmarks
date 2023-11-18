# Description
Microbenchmark containing one handler (`onHTTPPostEvent`) triggered by a HTTP request. This microbenchmark has been developed to detect [DynamoDB Injection](https://medium.com/appsecengineer/dynamodb-injection-1db99c2454ac) as reported by Bhargav. To identify the expected data flow, a Pysa model for the DynamoDB `scan` API has to be used. Note that the `boto3` interface object for DynamoDB is an instance of `boto3.client`.

# Expected Results
The analysis tool is expected to identify the following data flows:

* Source: `event` input argument in the definition of the handler `onHTTPPostEvent`, i.e., `def onHTTPPostEvent(event, context):`
* Sink: `ScanFilter=event['body']` (input argument of the `scan` API call in the handler `onHTTPPostEvent`)
