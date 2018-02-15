#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

from flask import Blueprint, redirect, request
from monolith.model import db
from stravalib import Client
from flask_login import current_user, login_required


stravaBp = Blueprint("strava", __name__)

@stravaBp.route("/strava_auth")
@login_required
def _strava_auth():
    code = request.args.get("code")
    client = Client()
    xc = client.exchange_code_for_token
    access_token = xc(client_id=stravaBp.app.config['STRAVA_CLIENT_ID'],
                     client_secret=stravaBp.app.config['STRAVA_CLIENT_SECRET'], code=code)
    current_user.strava_token = access_token
    db.session.add(current_user)
    db.session.commit()
    return redirect('/')
