import json
# arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p39-requests:6
import requests
import boto3
from botocore.config import Config

REQUEST_TIMEOUT = 7
BOTO3_CONNECT_TIMEOUT = 7

config = Config(
    retries={
        'max_attempts': 1,
        'mode': 'standard'
    },
    connect_timeout=BOTO3_CONNECT_TIMEOUT
)

s3 = boto3.client('s3', config=config)


def lambda_handler(event, context):
    try:
        url = 'https://ipinfo.io/ip'

        receive = requests.get(url, timeout=REQUEST_TIMEOUT)
        print('URL available')
        print('Content:')
        print(receive.content)
    except Exception as e:
        print('URL not available')
    try:
        response = s3.list_buckets()
        print('S3 access available')
    except Exception as e:
        print('S3 not available')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
