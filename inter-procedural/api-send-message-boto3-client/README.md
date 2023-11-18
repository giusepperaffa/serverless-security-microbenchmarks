# Description
Microbenchmark developed by using [api-put-item-boto3-client](../../dynamodb-service/api-put-item-boto3-client) as baseline. The key difference is that the functionality previously included _only_ within the handler `onHTTPPostEvent` has now been split between the latter and the handler `onSQSMessage` thanks to a SQS queue. **Note** that the `serverless.yml` file was updated by using the example included in the repository [mxnet-ci](https://github.com/apache/mxnet-ci/blob/master/services/github-bots/LabelBotFullFunctionality/serverless.yml), which is part of the [AWSomePy dataset](https://zenodo.org/record/7838077). 

# Expected Results
The analysis tool is expected to identify the following data flows:

* Source: `event` input argument in the definition of the handler `onHTTPPostEvent`, i.e., `def onHTTPPostEvent(event, context):`
* Sink: `os.system('echo %s' % eventData)` (handler `onDynamoDBStream`)
