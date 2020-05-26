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


def get_log_streams(log_group, start_limit=1, end_limit=20):

    log_streams = []

    client = boto3.client('logs')
    paginator = client.get_paginator('describe_log_streams')

    config = {
        'MaxItems': end_limit,
        'PageSize': 50
    }

    kwargs = {
            'logGroupName':log_group, 
            'orderBy':"LastEventTime",
            'descending':True,
    }
    for page in paginator.paginate(PaginationConfig = config, **kwargs):
        log_streams += page.get("logStreams")

    return log_streams[start_limit-1:]

if __name__ == '__main__':
    args = docopt.docopt(__doc__)

    log_group = args['<LOG_GROUP_NAME>']
    start_limit = 1
    end_limit = 20

    if args['--limit']:
        limit = args['--limit']
        if len(limit.split("-")) == 2:
            start_limit = int(limit.split("-")[0])
            end_limit = int(limit.split("-")[1])
        else:
            end_limit = int(limit)

    log_streams = get_log_streams(
        log_group=log_group,
        start_limit=start_limit,
        end_limit=end_limit,
    )

    number = start_limit
    for stream in log_streams:
        name = stream.get("logStreamName")
        creation_time = stream.get("creationTime")
        creation_time = datetime.datetime.fromtimestamp(int(creation_time)/1000)
        last_event_time = stream.get("lastEventTimestamp")
        last_event_time = datetime.datetime.fromtimestamp(int(last_event_time)/1000)
        print(f"{number}: name: {name}; creation_time: {creation_time}; last_event_time: {last_event_time}")
        number = number + 1
