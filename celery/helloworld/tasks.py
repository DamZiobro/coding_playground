#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

from celery import Celery

BROKER=BACKEND="amqp://damian:damian@localhost:5672/damianvhost"

app = Celery('tasks', broker=BROKER, backend=BACKEND)

@app.task
def add(x, y):
    return x+y
