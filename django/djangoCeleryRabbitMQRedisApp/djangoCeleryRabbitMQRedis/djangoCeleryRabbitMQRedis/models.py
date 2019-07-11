#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 damian <damian@damian-work>
#
# Distributed under terms of the MIT license.

from django.db import models


class Job(models.Model):  
    """Class describing a computational job"""

    # currently, available types of job are:
    TYPES = (
        ('fibonacci', 'fibonacci'),
        ('power', 'power'),
    )

    # list of statuses that job can have
    STATUSES = (
        ('pending', 'pending'),
        ('started', 'started'),
        ('finished', 'finished'),
        ('failed', 'failed'),
    )

    type = models.CharField(choices=TYPES, max_length=20)
    status = models.CharField(choices=STATUSES, max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    argument = models.PositiveIntegerField()
    result = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        """Save model and if job is in pending state, schedule it"""
        super(Job, self).save(*args, **kwargs)
        if self.status == 'pending':
            from .tasks import TASK_MAPPING
            task = TASK_MAPPING[self.type]
            task.delay(job_id=self.id, n=self.argument)
