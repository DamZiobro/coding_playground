#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

from flask import Blueprint
fetchBp = Blueprint('fetch', __name__)

@fetchBp.route("/fetch")
def fetch_runs():
    from monolith.background import fetch_all_runs
    res = fetch_all_runs.delay()
    res.wait()
    return jsonify(res.result)

