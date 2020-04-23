#!/usr/bin/env python
# -*- encoding: utf-8
"""Print log event messages from a CloudWatch log group.

Usage: aws_get_log_events.py <LOG_GROUP_NAME> [--log-stream=<LOG_STREAM_NAME>] [--start=<START>] [--end=<END>] [--limit=<LIMIT>] [--filter=<FILTER_PATTERN>]
       aws_get_log_events.py -h --help

Options:
  <LOG_GROUP_NAME>    Name of the CloudWatch log group.
  --log-stream=<LOG_GROUP_NAME>    Name of the CloudWatch log stream.
  --start=<START>     Only print events with a timestamp after this time.
  --end=<END>         Only print events with a timestamp before this time.
  --limit=<LIMIT>     Maximum number of messages to get
  --filter=<FILTER_PATTERN> Patter to filter messages
  -h --help           Show this screen.

"""

import boto3
import docopt
import maya
import re


def get_log_events(log_group, log_stream=None, start_time=None, end_time=None, limit=10000, filter=""):
    """Generate all the log events from a CloudWatch group.

    :param log_group: Name of the CloudWatch log group.
    :param start_time: Only fetch events with a timestamp after this time.
        Expressed as the number of milliseconds after midnight Jan 1 1970.
    :param end_time: Only fetch events with a timestamp before this time.
        Expressed as the number of milliseconds after midnight Jan 1 1970.

    """
    client = boto3.client('logs')
    if log_stream:
        kwargs = {
            'logGroupName': log_group,
            'logStreamNames': [log_stream],
            'limit': limit,
        }
    else:
        kwargs = {
            'logGroupName': log_group,
            'limit': limit,
        }

    if start_time is not None:
        kwargs['startTime'] = start_time
    if end_time is not None:
        kwargs['endTime'] = end_time

    while True:
        resp = client.filter_log_events(**kwargs)
        yield from resp['events']
        try:
            kwargs['nextToken'] = resp['nextToken']
        except KeyError:
            break


def milliseconds_since_epoch(time_string):
    dt = maya.when(time_string)
    seconds = dt.epoch
    return seconds * 1000


if __name__ == '__main__':
    args = docopt.docopt(__doc__)

    log_group = args['<LOG_GROUP_NAME>']

    log_stream = None
    start_time = None
    end_time = None
    limit = 10000
    filter=""

    if args['--log-stream']:
        log_stream = args['--log-stream']

    if args['--limit']:
        limit = int(args['--limit'])

    if args['--filter']:
        filter = args['--filter']

    if args['--start']:
        try:
            start_time = milliseconds_since_epoch(args['--start'])
        except ValueError:
            exit(f'Invalid datetime input as --start: {args["--start"]}')

    if args['--end']:
        try:
            end_time = milliseconds_since_epoch(args['--end'])
        except ValueError:
            exit(f'Invalid datetime input as --end: {args["--end"]}')

    logs = get_log_events(
        log_group=log_group,
        log_stream=log_stream,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
        filter=filter,
    )
    for event in logs:
        log_message = event['message'].rstrip()
        if re.search(filter, log_message):
            print(log_message)
