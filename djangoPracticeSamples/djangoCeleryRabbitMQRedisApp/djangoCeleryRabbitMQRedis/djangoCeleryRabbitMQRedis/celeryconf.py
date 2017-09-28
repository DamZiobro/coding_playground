#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 damian <damian@damian-work>
#
# Distributed under terms of the MIT license.

import os

from celery import Celery  
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoCeleryRabbitMQRedis.settings")

app = Celery('djangoCeleryRabbitMQRedis')

CELERY_TIMEZONE = 'UTC'

app.config_from_object('django.conf:settings')  
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)  

