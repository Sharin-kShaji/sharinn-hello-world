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
        temp_file = "/tmp/hello_local.txt"
        s3.Bucket(BUCKET_NAME).download_file(KEY, temp_file)
        file = open(temp_file, "r")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
