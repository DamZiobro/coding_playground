#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.
from flask import Blueprint, render_template
from stravalib import Client

from monolith.model import db, Run
from monolith.auth import current_user


homeBp = Blueprint('home', __name__)


def _strava_auth_url(config):
    client = Client()
    client_id = config['STRAVA_CLIENT_ID']
    redirect = 'http://127.0.0.1:5000/strava_auth'
    url = client.authorization_url(client_id=client_id,
                                   redirect_uri=redirect)
    return url


@homeBp.route('/')
def index():
    if current_user is not None and hasattr(current_user, 'id'):
        runs = db.session.query(Run).filter(Run.runner_id == current_user.id)
    else:
        runs = None
    strava_auth_url = _strava_auth_url(homeBp.app.config)
    return render_template("index.html", runs=runs,
                           strava_auth_url=strava_auth_url)
