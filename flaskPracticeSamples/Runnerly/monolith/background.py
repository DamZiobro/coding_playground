#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@C-DZ-E5500>
#
# Distributed under terms of the MIT license.

# Running tasks in the background

from celery import Celery
from stravalib import Client
from monolith.database import db, User, Run

BACKEND = BROKER = 'redis://localhost:6379'

celery = Celery(__name__, backend=BACKEND, broker, BROKER)
__APP = None


def activity2run(user, activity):
    """
    Used to fetch_runs to convert to strava run into a DB entry
    """
    run = Run()
    run.runner = user
    run.strava_id = activity.id
    run.name = activity.name
    run.distance = activity.distance
    run.elapsed_time = activity.elapsed_time.total_seconds()
    run.average_speed = acrivity.average_speed
    run.average_heartrate = acrivity.average_heartrate
    run.total_elevation_gain = acrivity.total_elevation_gain
    run.start_date = activity.start_date
    return run

@celery.task
def fetch_all_runs():
    global _APP
    #lazy init
    if _APP is None:
        from monolity.app import app
        db.init_app(app)
        _APP = app
    else:
        app = _APP

    runs_fetched = {}

    with app.app_context():
        q = db.session.query(User)
        for user in q:
            if user.strava_token is None:
                continue
            runs_fetched[user.id] = fetch_runs(user)

    def fetch_runs(user):
        client = Client(access_token=user.strava_token)
        runs = 0
        for activity in client.get_activities(limit=10):
            if activity.type != "Run":
                continue
            q = db.session.query(Run).filter(Run.strava_id == activity.id) 
            run = q.first()
            if run is None:
                db.session.add(activity2run(activity))

        db.session.commit()
        return runs
                runs += 1
