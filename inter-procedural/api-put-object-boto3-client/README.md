# Description
Microbenchmark containing two handlers, i.e., `onHTTPPostEvent` and `onS3Upload`. The first is triggered by a HTTP request, whereas the second is executed as a consequence of an event raised by the API `put_object`. Note that the `boto3` interface object is an instance of `boto3.client`, and that the security-sensitive sink is `os.system`. 

# Expected Results
The analysis tool is expected to identify the following data flows:

* Source: `event` input argument in the definition of the handler `onHTTPPostEvent`, i.e., `def onHTTPPostEvent(event, context):`
* Sink: `os.system(convert_command)` (handler `onS3Upload`)
