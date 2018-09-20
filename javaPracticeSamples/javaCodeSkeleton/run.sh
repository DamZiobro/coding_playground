#! /bin/bash
#
# run.sh

#exit immediately if any error
set -e

APP=$(basename $PWD)

# build and test
echo -e "======================================="
echo -e "BUILD AND TEST $APP"
echo -e "======================================="
gradle assemble test  

# run 
echo -e "\n"
echo -e "======================================="
echo -e "RUN $APP"
echo -e "======================================="
java -jar ./build/libs/$(basename $PWD).jar


