# Description
Microbenchmark developed by using [api-put-item-boto3-client](../api-put-item-boto3-client) as baseline. These are the differences:

* This microbenchmark includes an additional DynamoDB table (`DYNAMODB_MASTER_TABLE`). The YAML file does _not_ include any permissions for this particular resource.
* The helper function `updateDynamoDBTable` has been modified. It attempts to execute the API `put_item` on the new DynamoDB table.

As a consequence of the above change, the execution of the API `put_item` is _not_ allowed, and the analysis tool should _not_ detect the data flow present in the baseline.

# Expected Results
The analysis tool is expected to identify the following data flows:

* Source: None
* Sink: None
