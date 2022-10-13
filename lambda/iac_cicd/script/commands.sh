#!/bin/bash

aws cloudformation deploy --template-file lambda-template.yml --stack-name test-lambda --capabilities CAPABILITY_IAM


sam init --runtime python3.9
sam build
sam deploy --guided

aws cloudformation deploy --template-file codebuild-template.yml --stack-name test-lambda-deploy --capabilities CAPABILITY_IAM
