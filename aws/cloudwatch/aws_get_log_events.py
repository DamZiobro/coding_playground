#!/usr/bin/env python
# -*- encoding: utf-8
"""Print log event messages from a CloudWatch log group.

Usage: aws_get_log_events.py <LOG_GROUP_NAME> [--log-stream=<LOG_STREAM_NAME>] [--start=<START>] [--end=<END>] [--limit=<LIMIT>] [--filter=<FILTER_PATTERN>] [--regex=<REGEX_PATTERN>] [--log-streams-number=<LOG_STREAMS_NUMBER>] [--is_print=IS_PRINT]
       aws_get_log_events.py -h --help

Options:
  <LOG_GROUP_NAME>    Name of the CloudWatch log group.
  --log-stream=<LOG_GROUP_NAME>    Name of the CloudWatch log stream.
  --start=<START>     Only print events with a timestamp after this time.
  --end=<END>         Only print events with a timestamp before this time.
  --limit=<LIMIT>     Maximum number of messages to get
  --regex=<FILTER_PATTERN> Patter to regex messages
  --filter=<FILTER_PATTERN> Patter to filter messages
  --log-streams-number=<LOG_STREAMS_NUMBER> Number of recent logs streams to process
  --is_print=<IS_PRINT> Should logs be printed to the console
  -h --help           Show this screen.

"""

import boto3
import docopt
import maya
import re
import sys
import datetime
import concurrent.futures
import logging 
import os

client = boto3.client('logs')
logging.basicConfig(level=logging.INFO)

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_logs(log_group, stream, start_time=None, end_time=None, limit=10000, filter="", regex="", is_print="no"):

    LOG_DIR="/tmp/awslogs"

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if isinstance(stream, str):
        log_stream_name = stream
        filename = f"{LOG_DIR}/" + log_stream_name.split("/")[-1]
        logging.info(f"GETTING log stream name: {log_stream_name}; filename: {filename}")
    else:
        log_stream_name = stream.get("logStreamName")
        creation_time = stream.get("creationTime")
        creation_time = datetime.datetime.fromtimestamp(int(creation_time)/1000)
        last_event_time = stream.get("lastEventTimestamp")
        last_event_time = datetime.datetime.fromtimestamp(int(last_event_time)/1000)
        filename = f"{LOG_DIR}/" + log_stream_name.split("/")[-1]
        logging.info(f"GETTING log stream name: {log_stream_name}; filename: {filename}; creation_time: {creation_time}; last_event_time: {last_event_time}")

    kwargs = {
        'logGroupName': log_group,
        'logStreamNames': [log_stream_name],
        'limit': limit,
    }

    if start_time is not None:
        kwargs['startTime'] = start_time
    if end_time is not None:
        kwargs['endTime'] = end_time
    if filter != "":
        kwargs['filterPattern'] = filter

    file = open(filename, "w")
    while True:
        resp = client.filter_log_events(**kwargs)
        #yield from resp['events']
        for event in resp['events']:
            log_message = event['message'].rstrip()
            if re.search(regex, log_message):
                if(is_print.startswith("y")):
                    print(f"{log_stream_name} => {log_message}")
                file.write(log_message + "\n")

        try:
            kwargs['nextToken'] = resp['nextToken']
        except KeyError:
            file.close()
            break

    return log_stream_name



def get_log_events(log_group, log_stream=None, start_time=None, end_time=None, limit=10000, filter="", log_streams_number=1, regex="", is_print="no"):

    log_streams = [log_stream]
    if start_time is None and end_time is None and log_stream is None:
        response = client.describe_log_streams(
            logGroupName=log_group, 
            orderBy="LastEventTime",
            descending=True,
            limit=log_streams_number
        )

        log_streams = response.get("logStreams")

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        try:
            stream_futures = {executor.submit(get_logs, log_group, stream, start_time, end_time, limit, filter, regex, is_print): stream for stream in log_streams}
        except Exception as ex:
            logging.error(f"exception: {ex}")

        for future in concurrent.futures.as_completed(stream_futures):
            stream = stream_futures[future]
            resp = future.result()
            logging.info(f"finished getting logs from stream: {resp}")


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
    regex=""
    log_streams_number = 1
    is_print="no"

    if args['--log-stream']:
        log_stream = args['--log-stream']

    if args['--log-streams-number']:
        log_streams_number = int(args['--log-streams-number'])

    if args['--limit']:
        limit = int(args['--limit'])

    if args['--filter']:
        filter = args['--filter']

    if args['--regex']:
        regex = args['--regex']

    if args['--is_print']:
        is_print = args['--is_print']
        if is_print.startswith("y"):
            logging.getLogger().setLevel(logging.WARN)

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
        log_streams_number=log_streams_number,
        regex=regex,
        is_print=is_print,
    )
