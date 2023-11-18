# Description
Microbenchmark developed by using [api-put-item-boto3-client](../api-put-item-boto3-client) as baseline. These are the main differences:

* The code of the handler `onHTTPPostEvent` includes a different initialization for `uploadFileFolder`, which does _not_ match the folder specified in the YAML file for the `onS3Upload` handler (`prefix` tag).

As a consequence of the above change, the execution of the `onS3Upload` handler is _not_ triggered, and the analysis tool should _not_ detect the data flow present in the baseline.

# Expected Results
The analysis tool is expected to identify the following data flows:

* Source: None
* Sink: None
