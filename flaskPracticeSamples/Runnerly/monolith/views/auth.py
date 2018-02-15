#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

from flask import Blueprint, redirect, render_template
from monolith.forms import LoginForm
from monolith.model import db, User
from flask_login import (current_user, login_user, logout_user, login_required)

authBp = Blueprint('auth', __name__)

@authBp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email, password = form.data['email'], form.data['password']
        q = db.session.query(User).filter(User.email == email)
        user = q.first()
        if user is not None and user.authenticate(password):
            login_user(user)
            return redirect('/')
    return render_template('login.html', form=form)

@authBp.route("/logout")
def logout():
    logout_user()
    return redirect('/')
