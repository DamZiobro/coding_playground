#! /bin/bash
#
# compileAndRun.sh
# Copyright (C) 2019 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.
#

FILE_NAME= $(shell basename $(shell pwd))
JAR_FILE=$(FILE_NAME).jar

all: compile run

compile:
	kotlinc $(FILE_NAME).kt -include-runtime -d $(JAR_FILE)

run:
	java -jar $(JAR_FILE)

