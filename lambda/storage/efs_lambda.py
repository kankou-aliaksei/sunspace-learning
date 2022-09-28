MNT_DIR = '/mnt/efs'


def lambda_handler(event, context):
    with open(f'{MNT_DIR}/output.txt', 'w') as file:
        file.write('Hello, World!!!')

    with open(f'{MNT_DIR}/output.txt', 'r') as file:
        data = file.read().replace('\n', '')
        print(data)