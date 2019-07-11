#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

from setuptools import setup, find_packages

REQUIRES = [
    'enum34;python_version<"3.4"'
]

setup(
    name="standardlibrarytests",
    version="0.1.1",
    author="Damian Ziobro",
    author_email="damian@xmementoit.com",
    packages=find_packages(),
    install_requires=REQUIRES
)
