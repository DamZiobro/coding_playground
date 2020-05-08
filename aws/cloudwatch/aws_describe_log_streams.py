#!/usr/bin/env python
# -*- encoding: utf-8
"""Print log event messages from a CloudWatch log group.

Usage: aws_get_log_events.py <LOG_GROUP_NAME> [--limit=<LIMIT>]
       aws_get_log_events.py -h --help

Options:
  <LOG_GROUP_NAME>    Name of the CloudWatch log group.
  --limit=<LIMIT>     Maximum number of messages to get
  -h --help           Show this screen.

"""

import boto3
import docopt
import re
import datetime


def get_log_streams(log_group, limit=20):

    client = boto3.client('logs')
    response = client.describe_log_streams(
        logGroupName=log_group, 
        orderBy="LastEventTime",
        descending=True,
        limit=limit
    )
    return response.get("logStreams")

if __name__ == '__main__':
    args = docopt.docopt(__doc__)

    log_group = args['<LOG_GROUP_NAME>']
    limit = 20

    if args['--limit']:
        limit = int(args['--limit'])

    log_streams = get_log_streams(
        log_group=log_group,
        limit=limit,
    )
    for stream in log_streams:
        name = stream.get("logStreamName")
        creation_time = stream.get("creationTime")
        creation_time = datetime.datetime.fromtimestamp(int(creation_time)/1000)
        last_event_time = stream.get("lastEventTimestamp")
        last_event_time = datetime.datetime.fromtimestamp(int(last_event_time)/1000)
        print(f"name: {name}; creation_time: {creation_time}; last_event_time: {last_event_time}")
