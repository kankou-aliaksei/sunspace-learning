import boto3
import os

s3 = boto3.resource('s3')


def lambda_handler(event, context):
    files = os.listdir('/tmp')
    print(files)
    if 'image.jpg' in files:
        print('The image is cached')
        # process the file
    else:
        print('Download the image from S3')
        bucket = 'test-2348237482387423784234'
        key = 'Cat-example.jpg'
        s3.Bucket(bucket).download_file(key, '/tmp/image.jpg')
        # process the file

