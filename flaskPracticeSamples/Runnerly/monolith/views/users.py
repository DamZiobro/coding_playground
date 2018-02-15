#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@C-DZ-E5500>
#
# Distributed under terms of the MIT license.

from flask import Blueprint, redirect, render_template, request
from monolith.model import db, User
from monolith.forms import UserForm

usersBp = Blueprint('users', __name__)

@usersBp.route('/users')
def users():
    users = db.session.query(User)
    return render_template("users.html", users=users)

@usersBp.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_user = User()
            form.populate_obj(new_user)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/users')
    return render_template('create_user.html', form=form)
