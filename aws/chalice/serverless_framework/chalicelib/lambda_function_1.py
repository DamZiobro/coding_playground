#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

from chalice import Blueprint

lambda_function_1_blueprint = Blueprint(__name__)

@lambda_function_1_blueprint.on_sqs_message(queue='sqs-lambda_function_1')
def lambda_function_1(event, context):
    app.log.info("trigger lambda_function_1")

