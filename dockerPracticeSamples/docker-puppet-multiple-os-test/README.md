Docker + Puppet integration skeleton  (test on multiple OSes using docker containers)
=====

This Docker+Puppet integration skeleton allows you to test your application or puppet manifest on multiple
OSes. 

It creates series docker images based on multiple different operating systems and
execute puppet manifest file whitin created images. 

Currently following OSes are supported:
 - Ubuntu:14.04
 - Ubuntu:16.04
 - CentOS:6
 - CentOS:7
 - Fedora:25
 - Debian:7

Usage
----
1. Implement your configuration into install.pp file (or use default one which
   installs vim package only)
2. Create series of docker image for multiple OS using this command:
```
./buildAndRun vim-install-test
```
It may take few minutes. Please wait ...

3. After installing you should see series of docker images 'vim-install-test-OS-VERSION' created.
Run `docker images` command to see them.

Each image will have puppet/install.pp file executed. You can create container based on the image
using `docker run` command and test your application manually. You can also
extend this script to allow automatic tests of your application on multiple OSes

Run container from created image
-----
Sample `docker run` command to access Ubuntu-based container (container will be
removed just after you exit it):
```
docker run --rm=true --name vim-test-ubuntu-16-04 -i -t vim-install-test-ubuntu-16-04 /bin/bash
docker@a0e3abcfa905:~$ vim --version
```
If you see output of command `vim --version` it means that vim has been
successfully installed through puppet manifest file.

Enjoy!
------
