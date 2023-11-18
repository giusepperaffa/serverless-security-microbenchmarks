# Description
This microbenchmark was developed by using [api-put-item-table-assign](../api-put-item-table-assign) as baseline. These are the differences:

* The processing within the handler `onS3Upload` includes the generation of two output files. The variables `outputFileA` and `outputFileB` are used to store the paths of the generated files.
* The auxiliary function `updateDynamoDBTable` processes the paths of the generated output files. Consequently, the implementation of this function has changed.

**Note**: The objective of the above changes was to provide a different implementation of the functionality included in the baseline. The expected inter-procedural data flow is therefore the same.

**Important**: The analysis tool is **not** currently able to detect the expected data flow due to a taint propagation issue. Additional information on this topic is available on the pyre-check GitHub repository [issue 797](https://github.com/facebook/pyre-check/issues/797).

# Expected Results
The analysis tool is expected to identify the following data flows:

* Source: `event` input argument in the definition of the handler `onHTTPPostEvent`, i.e., `def onHTTPPostEvent(event, context):`
* Sink: `output = subprocess.check_output(cmd, shell=True, text=True)` (handler `onDynamoDBStream`)
