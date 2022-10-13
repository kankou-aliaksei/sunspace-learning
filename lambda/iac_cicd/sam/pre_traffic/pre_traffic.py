import boto3

code_deploy = boto3.client('codedeploy')


def lambda_handler(event, context):
    print(event)
    deployment_id = event['DeploymentId']
    life_cycle_event_hook_execution_id = event['LifecycleEventHookExecutionId']

    code_deploy.put_lifecycle_event_hook_execution_status(
        deploymentId=deployment_id,
        lifecycleEventHookExecutionId=life_cycle_event_hook_execution_id,
        status='Succeeded'  # 'Pending'|'InProgress'|'Succeeded'|'Failed'|'Skipped'|'Unknown'
    )
