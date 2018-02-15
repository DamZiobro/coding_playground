#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@C-DZ-E5500>
#
# Distributed under terms of the MIT license.

import os
from flask import Flask, render_template
from monolith.model import db, User
from monolith.views import blueprints
from monolith.auth import login_manager

def create_app():
    app = Flask(__name__)
    app.config['WTF_CSRF_SECRET_KEY'] = 'A SECRET KEY'
    app.config['SECRET_KEY'] = 'ANOTHER ONE'
    app.config['STRAVA_CLIENT_ID'] = os.environ['STRAVA_CLIENT_ID']
    app.config['STRAVA_CLIENT_SECRET'] = os.environ['STRAVA_CLIENT_SECRET']
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/runnerly'

    for bp in blueprints:
        app.register_blueprint(bp)
        bp.app = app

    db.init_app(app)
    login_manager.init_app(app)
    db.create_all(app=app)

    #create sample user
    with app.app_context():
        q = db.session.query(User).filter(User.email == "damian@example.com")
        user = q.first()
        if user is None:
            damian = User()
            damian.email = "damian@example.com"
            damian.is_admin = True
            damian.set_password('damian')
            db.session.add(damian)
            db.session.commit()

    return app

if __name__ == "__main__":    
    app = create_app()
    app.run()
