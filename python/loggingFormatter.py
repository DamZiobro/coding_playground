#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import re

class PasswordMaskingFormatter(logging.Formatter):
    """Mask username and password in mysql command"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.regexes_to_mask = [
            r"-p\'(?P<to_mask>.*)'",
            r"-u\s?(?P<to_mask>.*)\s+-p"
        ]

    def format(self, record):
        msg = super().format(record)
        for regex in self.regexes_to_mask:
            for match in re.finditer(regex, msg):
                string_to_mask = match.group('to_mask')
                masked_string = string_to_mask[0:1] + len(string_to_mask[1:]) * "*"
                msg = msg.replace(string_to_mask, masked_string)
        return msg


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
for handler in logger.handlers:
    handler.setFormatter(PasswordMaskingFormatter())

logging.info("damian")
text = """
mysqldump --skip-lock-tables --single-transaction
-h localhost -u USERNAME_TO_MASK -p\'PASSWORD_TO_MASK\' database_name
> /tmp/dump.sql
"""
logging.info(text)
