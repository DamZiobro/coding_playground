#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 damian <damian@damian-work>
#
from functools import wraps

from djangoCeleryRabbitMQRedis.celeryconf import app  
from .models import Job

# decorator to avoid code duplication

def update_job(fn):  
    """Decorator that will update Job with result of the function"""

    # wraps will make the name and docstring of fn available for introspection
    @wraps(fn)
    def wrapper(job_id, *args, **kwargs):
        job = Job.objects.get(id=job_id)
        job.status = 'started'
        job.save()
        try:
            # execute the function fn
            result = fn(*args, **kwargs)
            job.result = result
            job.status = 'finished'
            job.save()
        except:
            job.result = None
            job.status = 'failed'
            job.save()
    return wrapper


# two simple numerical tasks that can be computationally intensive

@app.task
@update_job
def power(n):  
    """Return 2 to the n'th power"""
    return 2 ** n


@app.task
@update_job
def fib(n):  
    """Return the n'th Fibonacci number.
    """
    if n < 0:
        raise ValueError("Fibonacci numbers are only defined for n >= 0.")
    return _fib(n)


def _fib(n):  
    if n == 0 or n == 1:
        return n
    else:
        return _fib(n - 1) + _fib(n - 2)

# mapping from names to tasks

TASK_MAPPING = {  
    'power': power,
    'fibonacci': fib
}

