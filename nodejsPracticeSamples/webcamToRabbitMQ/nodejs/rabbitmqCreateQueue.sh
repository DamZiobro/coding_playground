#!/bin/bash
# Author: Damian Ziobro <damian@xmementoit.com>
# Create RabbitMQ queue, exchange and binging

if [ -z $1 ]; then 
  echo "ERROR: wrong argument"
  echo "Usage: $0 queue_name"
  exit -1
fi
#queue name
NAME=$1

rabbitmqadmin declare exchange name=$NAME type=fanout durable=true 
rabbitmqadmin declare queue name=$NAME durable=true
rabbitmqadmin declare binding source=$NAME destination=$NAME routing_key=$NAME 
