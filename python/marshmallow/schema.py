#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

from marshmallow import Schema, fields, EXCLUDE
from pprint import pprint

class SaveSchema(Schema):
    class Meta: 
        unknown = EXCLUDE
    MCN = fields.Str(required=True)

class PersonalisationSchema(Schema):
    class Meta: 
        unknown = EXCLUDE
    MCN = fields.Str(required=True)

class ContextSchema(Schema):
    class Meta: 
        unknown = EXCLUDE
    field = fields.Raw(required=False)

class MarketingEmailSchema(Schema):
    email = fields.Str(required=True)
    save = fields.Nested(SaveSchema, required=False)
    personalisation = fields.Nested(PersonalisationSchema, required=False)
    context = fields.Nested(ContextSchema, required=True)

data = {
  "email": "string",
  "context": { } 
}

schema = MarketingEmailSchema()

result = schema.load(data)

pprint(result)

