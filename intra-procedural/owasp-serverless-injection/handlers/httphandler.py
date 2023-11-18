import boto3
import datetime
import os
import subprocess
import urllib


def onHTTPPostEvent(event, context):
    media_bucket = os.getenv('BUCKET_NAME')
    s3 = boto3.client('s3')
    list = s3.list_objects(Bucket=media_bucket)['Contents']
    for s3_key in list:
        key = urllib.unquote(s3_key['Key'].replace('+', ' ')).decode('utf8')
        now = datetime.datetime.now()
        fname = now.strftime("%Y%m%d%H%M%S") + '.jpg'
        fpath = '{year}/{month}/{day}/'.format(year=now.year, month=now.month, day=now.day)
        subprocess.call('mkdir -p /tmp/' + fpath, shell=True)
        if key.endswith(".jpg"):
            s3.download_file(media_bucket, key, '/tmp/' + fpath + fname)
        else:
            s3.download_file(media_bucket, key, '/tmp/' + key)
            convert_command = 'cd /tmp; convert {source} {path}{file}'.format(source=key, path=fpath, file=fname)
            subprocess.call(convert_command, shell=True)
            
