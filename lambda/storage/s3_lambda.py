import boto3
# arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p39-pillow:1
from PIL import Image
from io import BytesIO
# arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p39-numpy:7
import numpy


def lambda_handler(event, context):
    source_bucket = ''
    source_key = 'source.jpg'
    source_region_name = 'us-east-1'
    target_bucket = source_bucket
    target_key = 'target.jpg'
    target_region_name = 'us-east-1'

    image_array = read_image(source_bucket, source_key, source_region_name)
    write_image(image_array, target_bucket, target_key, target_region_name)


def read_image(bucket_name, key, region_name):
    s3 = boto3.resource('s3', region_name=region_name)
    bucket = s3.Bucket(bucket_name)
    obj = bucket.Object(key)
    response = obj.get()
    file_stream = response['Body']
    image_array = Image.open(file_stream)
    return numpy.array(image_array)


def write_image(image_array, bucket_name, key, region_name):
    s3 = boto3.resource('s3', region_name)
    bucket = s3.Bucket(bucket_name)
    s3_object = bucket.Object(key)
    file_stream = BytesIO()
    image = Image.fromarray(image_array)
    image.save(file_stream, format='jpeg')
    s3_object.put(Body=file_stream.getvalue())


if __name__ == '__main__':
    lambda_handler('', '')
