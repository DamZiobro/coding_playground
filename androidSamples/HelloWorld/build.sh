#! /bin/bash
#
# build.sh
# Copyright (C) 2017 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.
#

set -e

if [ ! -z $2 ]; then
  ./gradlew assembleDebug 
fi

if [ "$1" == "emulator" ]; then
  adb shell "am start -a android.intent.action.MAIN -n com.example.damian.helloworld/.MainActivity"
else
  adb -d install -r ./app/build/outputs/apk/app-debug.apk
  adb -d shell "am start -a android.intent.action.MAIN -n com.example.damian.helloworld/.MainActivity"
fi

