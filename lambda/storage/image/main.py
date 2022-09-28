import os


def lambda_handler(event, context):
    files = os.listdir('/data')
    print(files)

    with open(f'/tmp/output.txt', 'w') as file:
        file.write('Hello, World!!!')

    with open(f'/tmp/output.txt', 'r') as file:
        data = file.read().replace('\n', '')
        print(data)
