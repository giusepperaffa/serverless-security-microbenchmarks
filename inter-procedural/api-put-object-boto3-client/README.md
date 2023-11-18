# Description
Microbenchmark containing two handlers, i.e., `onHTTPPostEvent` and `onS3Upload`. The first is triggered by a HTTP request, whereas the second is executed as a consequence of an event raised by the API `put_object`. This microbenchmark is identical to [api-put-object-two-handlers](../api-put-object-two-handlers), except for the `boto3` interface object, which is an instance of `boto3.client` (rather than an instance of `boto3.resource`), and the security-sensitive sink, which is `os.system` (rather than `subprocess.call`). 

# Expected Results
The analysis tool is expected to identify the following data flows:

* Source: `event` input argument in the definition of the handler `onHTTPPostEvent`, i.e., `def onHTTPPostEvent(event, context):`
* Sink: `os.system(convert_command)` (handler `onS3Upload`)
