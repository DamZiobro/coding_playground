Android Hello World with JNI
============================

'Hello world' Android application using Gradle to build with native code runned
using JNI.

Prerequisities
--------
Please dont forget to authorize your USB plugged Android device to run your app
by adding following note to your `/etc/udev/rules.d/51-android.rules` file (this
adds vendorID 12d1 for Huawai device)
```
SUBSYSTEM=="usb", ATTR{idVendor}=="12d1", MODE="0666", GROUP="plugdev"
```
After adding this note plug out and plug in your USB device to your computer.

Build and Run on USB connected device
------
```
./build.sh device build
```
