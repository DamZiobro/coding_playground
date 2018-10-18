#! /bin/bash
#
# build.sh
# Copyright (C) 2018 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.
#


docker build -t xmementoit/android-sdk $PWD/android-sdk
docker build -t xmementoit/android-studio $PWD/android-studio

