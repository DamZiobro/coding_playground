#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

from typing import NewType

UserId = NewType('UserId', int)

some_id1 = UserId(524313)
print(f"someId1: {some_id1}")

#typing is not strong, it's only suggestion, so we still can pass 'string'
some_id2 = UserId("aaa")
print(f"someId2: {some_id2}")


