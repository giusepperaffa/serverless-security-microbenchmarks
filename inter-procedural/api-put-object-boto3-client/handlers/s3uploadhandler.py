# ---------------------
# Import Python Modules
# ---------------------
import os

# -------
# Handler
# -------
def onS3Upload(event, context):
    # ---------------------------
    # Retrieve uploaded file name
    # ---------------------------
    filesUploaded = event['Records']
    for fileUploaded in filesUploaded:
        # The following statement retrieves the filename that includes
        # the name of the folder within the S3 bucket.
        fileName = fileUploaded["s3"]["object"]["key"]
        bucketName = fileUploaded["s3"]["bucket"]["name"]
        print('--- The following file was uploaded %s ---' % fileName)
    # ------------
    # Process file
    # ------------
    convert_command = 'cd /tmp; convert {old_file} {new_file}'.format(old_file = fileName, new_file = bucketName + '_' + fileName)
    os.system(convert_command)
    return

