#! /usr/bin/env python

import fire
import boto3
import logging
from boto3.dynamodb.conditions import Key, Attr

"""
Example usage:
    python dynamodb_query.py --table_name="dev.orders" --query_key="orderDate" --query_value="10122020"
"""

def query_dynamodb(table_name, query_key, query_value):
    print(f"Querying dynamodb table: {table_name} with filter => {query_key}={query_value}")
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    response = table.query(
        KeyConditionExpression=Key(str(query_key)).eq(str(query_value))
    )

    for item in response['Items']:
        print(str(item))

    items_number = len(response['Items'])
    print(f"number of items for query '{query_key}={query_value}': {items_number}")

if __name__ == "__main__":
    fire.Fire(query_dynamodb)
