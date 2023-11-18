# Description
Microbenchmark developed by including one the injection-related attack scenarios illustrated in the [OWASP Top 10 Interpretation for Serverless document](https://raw.githubusercontent.com/OWASP/Serverless-Top-10-Project/master/OWASP-Top-10-Serverless-Interpretation-en.pdf) in a Serverless Framework-compatible application.

# Expected Results
The analysis tool is expected to identify the following data flows:

* Source: `list = s3.list_objects(Bucket=media_bucket)['Contents']` (handler `onHTTPPostEvent`)
* Sink: `subprocess.call(convert_command, shell=True)` (handler `onHTTPPostEvent`)
