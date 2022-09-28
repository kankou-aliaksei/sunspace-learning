def lambda_handler(event, context):
    with open('/opt/python/file.txt', 'r') as file:
        data = file.read().replace('\n', '')
        print(data)