#! /bin/bash
#
# run.sh
# Copyright (C) 2018 damian <damian@C-DZ-E5500>
#
# Distributed under terms of the MIT license.
#

if ! $(whereis bandit &> /dev/null); then
  echo -e "Installing bandit"
  sudo pip install bandit
fi

bandit insecureCode.py


