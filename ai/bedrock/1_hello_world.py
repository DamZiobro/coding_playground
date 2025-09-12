#! /usr/bin/env python

import json
import boto3

bedrock = boto3.client("bedrock")
bedrock_runtime = boto3.client("bedrock-runtime")
# List available foundation models
models = bedrock.list_foundation_models()
print(json.dumps(models["modelSummaries"], indent=4))

prompt = (
    "You are a seasoned software engineer and AI tutor. "
    "Explain the concept of vector embeddings in bullet points, "
    "using simple language suitable for a developer transitioning into AI."
)
response = bedrock_runtime.invoke_model(
    modelId='amazon.titan-text-express-v1',
    contentType='application/json',
    accept='application/json',
    body=json.dumps({
        'prompt': "Explain recursion in simple terms",
        'maxTokens': 150,
        'temperature': 0.2,
    })
)
print(response['Body'])
