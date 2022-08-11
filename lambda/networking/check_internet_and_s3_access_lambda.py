import json
import requests
import boto3

s3 = boto3.client('s3')


def lambda_handler(event, context):
    try:
        receive = requests.get('https://ipinfo.io/ip')
        print('Public internet available')
        print('Content:')
        print(receive.content)
    except Exception as e:
        print('Public internet not available')
    try:
        response = s3.list_buckets()
        print('S3 access available')
    except Exception as e:
        print('S3 not available')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
