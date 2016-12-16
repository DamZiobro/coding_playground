#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 damian <damian@damian-work>
#
# Distributed under terms of the MIT license.

import pyautogui
import sys

if __name__ == "__main__":    
    if len(sys.argv) != 2:
        print("ERROR: wrong argument")
        print("      Usage: " + str(sys.argv[0]) + " image.png")
        sys.exit(-1)

    print("recognizing image: " + sys.argv[1])
    print(pyautogui.locateOnScreen(sys.argv[1]))
    
