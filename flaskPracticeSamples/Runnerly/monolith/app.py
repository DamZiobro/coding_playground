#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@C-DZ-E5500>
#
# Distributed under terms of the MIT license.


from flask import Flask, render_template
from monolith.model import db, User
from monolith.views import blueprints

def create_app():
    app = Flask(__name__)

    for bp in blueprints:
        app.register_blueprint(bp)
        bp.app = app

    db.init_app(app)
    db.create_all(app=app)

    return app

if __name__ == "__main__":    
    app = create_app()
    app.run()
