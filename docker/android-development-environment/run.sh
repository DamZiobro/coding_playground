#! /bin/bash
#
# run_docker.sh

#!/bin/sh
# $1 - container name
# $2 - command to run (optional)
docker images | grep android-studio &> /dev/null
if [ $? != 0 ]; then
  echo -e "android-studio docker image not found - building it..."
  ./build.sh
fi

sudo docker run -it --privileged \
    -e DISPLAY \
    -v /dev/bus/usb:/dev/bus/usb \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /vagrant:/vagrant \
    -v $HOME/AndroidStudioProjects/:/home/android/AndroidStudioProjects \
    --group-add plugdev \
    --name "android-studio" \
    "xmementoit/android-studio" /bin/bash

