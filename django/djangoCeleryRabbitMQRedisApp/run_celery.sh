#! /bin/bash
#
# run_celery.sh
# Copyright (C) 2017 damian <damian@damian-work>

# wait for RabbitMQ server to start
sleep 10

cd djangoCeleryRabbitMQRedis  
# run Celery worker for our project djangoCeleryRabbitMQRedis with Celery configuration stored in Celeryconf
su -m myuser -c "celery worker -A djangoCeleryRabbitMQRedis.celeryconf -Q default -n default@%h"  

