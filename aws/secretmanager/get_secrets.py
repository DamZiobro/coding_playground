#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

import boto3

if __name__ == "__main__":
    client = boto3.client('secretsmanager')

    response = client.describe_secret(
        SecretId='dev-simple-book-catalog-AuroraClusterSecret'
    )

    print(response)
