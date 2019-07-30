#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 damian <damian@C-DZ-E5500>
#
# Distributed under terms of the MIT license.
'''
setup config for Flask helloworld app
'''

import sys
import os

from setuptools import setup
from setuptools.command.test import test as TestCommand

install_requires = [
    'flask==1.0.0'
    ]

test_requires = [
    'pytest>=2.8.0',
    'pytest-xdist',
    'pytest-cov',
    'pytest-mock',
    'pytest-pylint',
    'pytest-bandit'
    ]

packages = ['helloworld']

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        try:
            from multiprocessing import cpu_count
            self.pytest_args = ['-n', str(cpu_count()), '--boxed']
        except (ImportError, NotImplementedError):
            self.pytest_args = ['-n', '1', '--boxed']

        # add pylint - static code analyser
        homepylintrc = os.getenv('HOME').join('.pylintrc')
        pylintrc = (
            homepylintrc \
            if os.path.exists(homepylintrc) \
            else 'tox.ini' \
            )
        self.pytest_args += ['--pylint', '--pylint-rcfile', pylintrc]

        # add coverage options - test coverage analyzer
        for package in packages:
            self.pytest_args += ['--cov', package]

        # add bandit - security scanner
        self.pytest_args += ['--bandit']

        # print pytest args as string
        print("pytest_args: {}".format(' '.join(self.pytest_args)))



    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name="hello-world",
    version="0.1.1",
    author="Damian Ziobro",
    author_email="damian@xmementoit.com",
    install_requires=install_requires,
    cmdclass={'test':PyTest},
    tests_require=test_requires,
    packages=packages,
)
