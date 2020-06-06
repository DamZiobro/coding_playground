#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.


import boto3
import datetime
import time
import logging
import argparse

logging.basicConfig(level=logging.INFO)

def time_interval_to_timedelta(time_interval):
    time_value = time_interval[0:-1]
    time_unit = time_interval[-1]

    if time_unit == "m":
        return datetime.timedelta(minutes=int(time_value))
    if time_unit == "h":
        return datetime.timedelta(hours=int(time_value))
    if time_unit == "d":
        return datetime.timedelta(days=int(time_value))

def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.datetime.fromtimestamp(now_timestamp) - datetime.datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

APPNAMES = ['homedelivery', "lambda_api", "homedelivery_all", "spaceadapter", "baskethandler", "orderadapter"]

def get_log_groups_of_app(appname, env):
   
    if not appname in APPNAMES:
        logging.error(f"undefined appname selected: '{appname}'. Only those appnames are defined: {APPNAMES}")
        return None
        
    if appname == "homedelivery":
        return [
                f"clg-euw1-{env}-storepick-os-bp-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-atp-s3_processing",
                f"/aws/lambda/lmb-euw1-{env}-digital-atp-bq-lambda-trigger",
                f"/aws/lambda/lmb-euw1-{env}-digital-atp-ecs-task-trigger",
            ]
    elif appname == "lambda_api":
        return [
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchCancel-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchCreate-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchDocGet-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchLatest-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchPatchItems-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchPostItems-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchPostLocations-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchStartProc-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchStatusGet-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-customer_collect_get_001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-customer_collect_put_001",
            ]
    elif appname == "homedelivery_all":
        return [
                f"clg-euw1-{env}-storepick-os-bp-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-atp-s3_processing",
                f"/aws/lambda/lmb-euw1-{env}-digital-atp-bq-lambda-trigger",
                f"/aws/lambda/lmb-euw1-{env}-digital-atp-ecs-task-trigger",
                #f"clg-euw1-{env}-storepick-mock-servers-mocks-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchCancel-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchCreate-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchDocGet-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchLatest-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchPatchItems-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchPostItems-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchPostLocations-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchStartProc-001",
                f"/aws/lambda/lmb-euw1-{env}-digital-strpck-batchStatusGet-001",
            ]
    elif appname == "spaceadapter":
        return [
            f"spaceadapter-{env}"
        ]
    elif appname == "orderadapter":
        return [
            f"order-adapter-task-{env}",
            f"/aws/lambda/OrderAdapterLambda-{env.upper()}"
        ]
    elif appname == "baskethandler":
        return [
            f"basket-handler-task-{env}"
        ]
    else:
        logging.error(f"Not found log groups for {appname} in {env}")
        return None

def is_recent_event_achieved(recent_log_event, log_event):

    if recent_log_event == None:
        return True

    log_fields = {field['field'] : field['value'] for field in log_event}
    recent_log_fields = {field['field'] : field['value'] for field in recent_log_event}

    for field in log_fields.keys():
        if log_fields.get(field) != recent_log_fields.get(field):
            return False

    return True


def get_logs(env, startTime, endTime ,query, limit, appname=None, log_groups=None):
    client = boto3.client('logs')

    if appname:
        log_groups = get_log_groups_of_app(appname, env)

    if not log_groups:
        logging.error("log_groups list is empty")
        return

    MAX_SINGLE_QUERY_LIMIT=10000
    results = { 'results' : [] }
    recent_timestamp = None
    recent_log_event = None

    filename = "/tmp/default_aws_insights_logs"
    if appname:
        filename = "/tmp/appname"

    output_file = open(filename, "w+")

    while len(results['results']) in (0, MAX_SINGLE_QUERY_LIMIT):
        if recent_timestamp:
            startTime = datetime.datetime.strptime(str(recent_timestamp), "%Y-%m-%d %H:%M:%S.%f")
            startTime = datetime_from_utc_to_local(startTime)

        #print(f"recent_timestamp: {recent_timestamp}")
        #print(f"startTime: {startTime.timestamp()}")
        #print(f"endTime: {endTime.timestamp()}")

        start = response = client.start_query(
                logGroupNames = log_groups,
                startTime = int(startTime.timestamp()),
                endTime = int(endTime.timestamp()),
                queryString = query,
                limit = limit
            )

        status = 'Init'
        while status not in ('Complete', 'Failed','Cancelled', 'Timeout'):
            logging.info("waiting for query results")
            time.sleep(10)
            results = client.get_query_results(queryId=start['queryId'])
            status = results['status']


        should_print_log_event = False
        for log_event in results['results']:
            log_fields = {field['field'] : field['value'] for field in log_event}

            line = ""
            for field in log_fields.keys():
                if field != "@ptr":
                    line += f"{log_fields[field]} "
            line = line.rstrip()

            if not should_print_log_event:
                should_print_log_event = is_recent_event_achieved(recent_log_event, log_event)
            else:
                print(line)
                output_file.write(line)

            recent_timestamp = log_fields.get('@timestamp')

        #if len(results['results']) > 0:
        recent_log_event = results['results'][-1]

    output_file.close()

if __name__ == "__main__":    

    parser = argparse.ArgumentParser()
    parser.add_argument('--env', help='test env name. Default: dev', default="dev")
    parser.add_argument('--limit', help='limit of messages', type=int, default=10000)

    parser.add_argument('--timedelta', help='delta time since now ex. 120m, 3h, 2d. Default: 60m', default="60m")

    parser.add_argument('--start', help='start time in the format of: YYYY-MM-DD HH:MM:SS')
    parser.add_argument('--end', help='end in the format of: YYYY-MM-DD HH:MM:SS')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--appname', help=f'name of the app which logs should be analysed. Defined apps: {APPNAMES}')
    group.add_argument('--log_groups', help='list of the log groups to analyse (up to 20)', nargs="+")

    parser.add_argument('--filter', help='regex filter for the default query', default="")

    default_query = f"fields @timestamp, @message | filter @message like // | sort @timestamp" 
    parser.add_argument('--query', help=f'insights query. Default: {default_query}', default=default_query)
    args = parser.parse_args()

    if args.query == default_query:
        args.query = f"fields @timestamp, @message | filter @message like /{args.filter}/ | sort @timestamp" 

    startTime  = None
    endTime = None

    if args.start and not args.end:
        startTime = datetime.datetime.strptime(args.start, "%Y-%m-%d %H:%M:%S")
        endTime = datetime.datetime.now()
    if args.start and args.end:
        startTime = datetime.datetime.strptime(args.start, "%Y-%m-%d %H:%M:%S")
        endTime = datetime.datetime.strptime(args.end, "%Y-%m-%d %H:%M:%S")
    elif args.timedelta:
        endTime = datetime.datetime.now()
        startTime = endTime - time_interval_to_timedelta(args.timedelta)
    else:
        logging.error("ERROR => Neither start/end pair nor timedelta is defined")
        parser.print_help()

    get_logs(args.env, startTime, endTime, args.query, args.limit, args.appname, args.log_groups)

