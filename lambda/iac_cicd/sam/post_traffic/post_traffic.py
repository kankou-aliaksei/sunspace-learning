import boto3
import json
import os

code_deploy = boto3.client('codedeploy')
lambda_client = boto3.client('lambda')

LAMBDA_ARN = os.environ['LAMBDA_ARN']


def lambda_handler(event, context):
    print(event)
    deployment_id = event['DeploymentId']
    life_cycle_event_hook_execution_id = event['LifecycleEventHookExecutionId']

    try:
        invoke_lambda_sync(LAMBDA_ARN, {})
    except:
        status = 'Failed'
    else:
        status = 'Succeeded'

    code_deploy.put_lifecycle_event_hook_execution_status(
        deploymentId=deployment_id,
        lifecycleEventHookExecutionId=life_cycle_event_hook_execution_id,
        status=status  # 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
    )


def invoke_lambda_sync(function_name, request_payload):
    response = lambda_client.invoke(
        FunctionName=function_name,
        Payload=json.dumps(request_payload)
    )

    if response['StatusCode'] != 200:
        raise Exception('Error. StatusCode: ' + response['StatusCode'])

    payload_string = response["Payload"].read()

    payload_object = json.loads(payload_string)

    if payload_object is not None and payload_object.get('errorMessage') is not None:
        error_message = payload_object['errorMessage']
        stack_trace = payload_object['stackTrace']
        raise Exception(f'{error_message}: {str(stack_trace)}')

    return payload_object
