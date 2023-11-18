# Description
Microbenchmark containing two handlers, i.e., `onHTTPPostEvent` and `onS3Upload`. The first is triggered by a HTTP request, whereas the second is executed as a consequence of an event raised by the API `put_object` called on the `Bucket` object. This microbenchmark is identical to [api-put-object-two-handlers](../api-put-object-two-handlers), except for the way the `Bucket` object is initialized. In this case, the handler `onHTTPPostEvent` includes a dedicated assignment that results in an intermediate `Bucket` object on which the API `put_object` is called.

# Expected Results
The analysis tool is expected to identify the following data flows:

* Source: `event` input argument in the definition of the handler `onHTTPPostEvent`, i.e., `def onHTTPPostEvent(event, context):`
* Sink: `subprocess.call(convert_command, shell=True)` (handler `onS3Upload`)
