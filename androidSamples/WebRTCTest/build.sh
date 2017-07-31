#! /bin/bash
#
# build.sh
# Copyright (C) 2017 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.
#

set -e

if [ ! -z $1 ]; then
  ./gradlew assembleDebug 
fi
adb -d install -r ./app/build/outputs/apk/app-arm-debug.apk
adb -d shell "am start -a android.intent.action.MAIN -n com.example.max.websockettest/.MainActivity"

