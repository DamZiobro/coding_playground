#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.
"""
Module contains classes responsible for textprocessing
"""

import string

class TextProcessor(object):
    """
    Class to test TextProcessing
    """

    @staticmethod
    def capitalize(text):
        '''Function capitalizes input string'''
        return string.capwords(text)
