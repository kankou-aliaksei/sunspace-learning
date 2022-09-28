FROM public.ecr.aws/lambda/python:3.8

COPY main.py .
COPY data /data
CMD ["main.lambda_handler"]