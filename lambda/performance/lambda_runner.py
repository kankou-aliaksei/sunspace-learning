import time
from multiprocessing.pool import ThreadPool as Pool
import boto3
import json

lambda_client = boto3.client('lambda')

CONCURRENCY = 8
LAMBDA_FUNC = 'test'


def get_timestamp():
    return int(round(time.time() * 1000))


def run_lambda(index, event):
    start_time = get_timestamp()
    lambda_client.invoke(
        FunctionName=LAMBDA_FUNC,
        Payload=json.dumps(event)
    )
    now_time = get_timestamp()
    diff = now_time - start_time
    print(f'Execution time: {str(diff)}. ID: {index}')


def run(event):
    pool = Pool(CONCURRENCY)
    for i in range(CONCURRENCY):
        pool.apply_async(run_lambda, (i, event))
    pool.close()
    pool.join()


run({})
