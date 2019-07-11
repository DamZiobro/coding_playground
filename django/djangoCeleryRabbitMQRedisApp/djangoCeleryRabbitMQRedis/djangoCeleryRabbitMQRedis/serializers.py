#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 damian <damian@damian-work>
#
# Distributed under terms of the MIT license.

from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = Job

