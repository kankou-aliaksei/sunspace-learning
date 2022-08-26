# arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p39-mysql-connector-python:2
import mysql.connector
import os

DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
DB_DATABASE = os.getenv('DB_DATABASE', 'test_db')
DB_TABLE = os.getenv('DB_TABLE', 'users')

cnx = mysql.connector.connect(
    user=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_DATABASE
)


def lambda_handler(event, context):
    print(f'Request ID: {context.aws_request_id}')

    cursor = cnx.cursor()

    record_id = 1

    cursor.execute(f"SELECT id, username, created_at FROM {DB_TABLE} WHERE id = {record_id}")

    for (record_id, username, created_at) in cursor:
        print(record_id, username, created_at)

    cursor.close()
    # cnx.close()
