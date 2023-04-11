import logging

def hello(event, context):

    msg = "MESSAGE PASS TO SQS QUEUE- CHANGE"
    logging.warning(msg)
    return msg

def hello2(event, context):

    msg = "MESSAGE PASS TO SQS QUEUE- CHANGE - LAMBDA2"
    logging.warning(msg)
    return msg
