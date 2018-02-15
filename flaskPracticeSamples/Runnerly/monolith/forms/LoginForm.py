#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

from flask_wtf import FlaskForm
import wtforms as f
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = f.StringField('email', validators=[DataRequired()])
    password = f.PasswordField('password', validators=[DataRequired()])
    display = ['email', 'password']
