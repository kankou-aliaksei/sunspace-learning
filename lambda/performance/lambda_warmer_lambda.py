import time
from multiprocessing import Process, Pipe
import boto3
import json

CONCURRENCY_LEVEL = 5
FUNCTION_NAME = 'test'


class Parallel:
    def __init__(self):
        self.lambda_client = boto3.client('lambda')

    def run_lambda(self, conn, index, event):
        self.lambda_client.invoke(
            FunctionName=FUNCTION_NAME,
            Payload=json.dumps(event),
            InvocationType='Event'
        )
        print(f'Thread ID: {index}')
        conn.close()

    def run(self, event):
        # create a list to keep all processes
        processes = []

        # create a list to keep connections
        parent_connections = []

        # create a process per instance
        for i in range(CONCURRENCY_LEVEL):
            # create a pipe for communication
            parent_conn, child_conn = Pipe()
            parent_connections.append(parent_conn)

            # create the process, pass instance and connection
            process = Process(target=self.run_lambda, args=(child_conn, i, event))
            processes.append(process)

        # start all processes
        for process in processes:
            process.start()

        # make sure that all processes have finished
        for process in processes:
            process.join()


def lambda_handler(event, context):
    parallel = Parallel()
    event = {
        'is_warmer': True
    }
    parallel.run(event)
