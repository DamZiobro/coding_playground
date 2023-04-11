import json
import logging
import boto3
import os


def hello(event, context):

    msg = "MESSAGE PASS TO SQS QUEUE"
    logging.warning(msg)
    sqs = boto3.client('sqs')
    sqs.send_message(
        QueueUrl=os.getenv("SQS_URL"),
        MessageBody=msg
    )
    return msg

def hello2(event, context):
    logging.warning(event)
    return event
