#! /bin/bash
#
# build.sh

gcc -Wall main.c -o playAudio $(pkg-config --cflags --libs gstreamer-1.0)

