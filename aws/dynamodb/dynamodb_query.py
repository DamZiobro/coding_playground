#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

import boto3
import datetime
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
table = dynamodb.Table('dev.xxwmm.storepick.items_v2')

batch_id = "16"

start_time = datetime.datetime.now()
print("Start index-based DB query...")
resp = table.query(
    IndexName = 'batchId-index',
    KeyConditionExpression=Key('batchId').eq(batch_id)
)
end_time = datetime.datetime.now()

delta = end_time - start_time
print(f"index-based query took: {delta}")
print(f"got {len(resp['Items'])} items for batch_id {batch_id}")

start_time = datetime.datetime.now()
print("Start non-index-based DB queries...")

items_list = []
NUMBER_ITEMS_PARTITION = 50
for index in range(0, NUMBER_ITEMS_PARTITION + 1):
    tmp_resp = table.query(
        KeyConditionExpression=Key('outOfStock').eq(f'outOfStock_{batch_id}_{index}'),
        ConsistentRead=True
    )
    items_list += tmp_resp['Items']

resp = {}
resp['Items'] = items_list

# THE BELOW QUERY THROWS EXCEPTION AS ONLY `eq` is allowed for KeyConditionExpression here...
#resp = table.query(
    #KeyConditionExpression=Key('outOfStock').begins_with('outOfStock_{batch_id}'),
    #ConsistentRead=True
#)
end_time = datetime.datetime.now()

delta = end_time - start_time

print(f"no-index-based query took: {delta}")
print(f"got {len(resp['Items'])} items for batch_id {batch_id}")

#print("The query returned the following items:")
#for item in resp['Items']:
    #print(item)

#config_table = dynamodb.Table('dev.xxwmm.storepick.config')

#response_array = []
#for status in ['NEW', 'PENDING', 'ITEMS_REVIEW', 'ITEMS_UPLOADED', 'IN_PROGRESS', 'CANCELLED', 'COMPLETED']:
    #table_items = config_table.query(
        #IndexName = 'status-index',
        #KeyConditionExpression = Key('status').eq(status),
    #)
    #response_array = response_array + (table_items['Items'])

#print(len(response_array))

