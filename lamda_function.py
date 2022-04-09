import json
import boto3
import botocore

import logging
logging.getLogger().setLevel(logging.INFO)


BUCKET_NAME = 'dev-days-test' # replace with your bucket name
KEY = 'hello.txt' # replace with your object key

s3 = boto3.resource('s3')

# TODO implement
def lambda_handler(event, context):
    logging.info(event)
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, '/tmp/hello_local.txt')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
