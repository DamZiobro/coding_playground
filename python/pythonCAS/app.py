#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

import logging
#import requests
from flask import Flask, request, session, redirect, url_for
from cas import CASClient

app = Flask(__name__)
app.secret_key = 'V7nlCN90LPHOTA9PGGyf'


logging.basicConfig(level=logging.DEBUG)


cas_client = CASClient(
    version=3,
    #service_url="https://genre-test.malariagen.net/accounts/login/",
    service_url="http://www.conflux.malariagen.net/login?next=%2Fprofile",
    server_url="https://www.malariagen.net/sso/login",
    proxy_callback="https://www.malariagen.net/sso/p3/proxyValidate",
    username_attribute="mail",
)


@app.route('/')
def index():
    """"""
    app.logger.debug(f"request.args => index: {request.args}")
    return redirect(url_for('login'))


@app.route('/profile')
def profile(method=['GET']):
    if 'username' in session:
        return 'Logged in as %s. <a href="/logout">Logout</a>' % session['username']
    return 'Login required. <a href="/login">Login</a>', 403


@app.route('/login')
def login():
    if 'username' in session:
    # Already logged in
     return redirect(url_for('profile'))


    app.logger.debug(f"request.args => login: {request.args}")
    next = request.args.get('next')
    ticket = request.args.get('ticket')
    if not ticket:
        # No ticket, the request come from end user, send to CAS login
        cas_login_url = cas_client.get_login_url()
        app.logger.debug('CAS login URL: %s', cas_login_url)
        return redirect(cas_login_url)

    # There is a ticket, the request come from CAS as callback.
    # need call `verify_ticket()` to validate ticket and get user profile.
    app.logger.debug('ticket: %s', ticket)
    app.logger.debug('next: %s', next)

    user, attributes, pgtiou = cas_client.verify_ticket(ticket)
    app.logger.debug(f"user: {user}; attributes: {attributes}; pgtiou: {pgtiou}")

    #proxy_ticket = cas_client.get_proxy_ticket(pgtiou)
    #app.logger.debug(f"proxy_ticket: {proxy_ticket}")

    #requests.get("https://genre-test.malariagen.net/accounts/login/?ticket=ST-4632-Y-VpT5fMihLPBO1E80FUxjj1rsoip-172-30-0-175")


    #app.logger.debug(
        #'CAS verify ticket response: user: %s, attributes: %s, pgtiou: %s', user, attributes, pgtiou)

    if not user:
        return 'Failed to verify ticket. <a href="/login">Login</a>'
    else:  # Login successfully, redirect according `next` query parameter.
        session['username'] = user
    return redirect(next)


@app.route('/logout')
def logout():
    redirect_url = url_for('logout_callback', _external=True)
    cas_logout_url = cas_client.get_logout_url(redirect_url)
    app.logger.debug('CAS logout URL: %s', cas_logout_url)

    return redirect(cas_logout_url)


@app.route('/logout_callback')
def logout_callback():
    # redirect from CAS logout request after CAS logout successfully
    session.pop('username', None)
    return 'Logged out from CAS. <a href="/login">Login</a>'
