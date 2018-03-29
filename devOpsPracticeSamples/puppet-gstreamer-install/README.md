Puppet manifest file to install GStreamer
=====

This Docker+Puppet integration skeleton allows you to test your application or puppet manifest on multiple
OSes. 

It allows to install GStreamer package + GStreamer plugins on multiple OSes and test them using
Docker images.

Currently following OSes are supported:
 - Ubuntu:14.04
 - Ubuntu:16.04
 - Debian:7

Usage
----
1. Create series of docker image for multiple OS using this command:
```
./buildAndRun gstreamer-install
```
It may take long time (up to around 1 hour or more). Please wait ...

2. After installing you should see series of docker images 'gstreamer-install-OS-VERSION' created.
Run `docker images` command to see them.

Each image will have puppet/install.pp file executed. You can create container based on the image
using `docker run` command and test your application manually. You can also
extend this script to allow automatic tests of your application on multiple OSes

Run container from created image
-----
Sample `docker run` command to access Ubuntu-based container (container will be
removed just after you exit it):
```
docker run --rm=true --name gstreamer-install -i -t gstreamer-install-ubuntu-16-04 /bin/bash
docker@a0e3abcfa905:~$ gst-inspect-1.0 --version
```
If you see output of command `gst-inspect-1.0 --version` it means that vim has been
successfully installed through puppet manifest file.

Vagrant box
----
Corresponding Vagrant box based on Vagrantfile from vagrant directory has been uploaded to Vagrant Cloud. 
You can find it here: 
https://app.vagrantup.com/xmementoit/boxes/gstreamer1.14 

Enjoy!
------
