#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 damian <damian@damian-work>
#
# Distributed under terms of the MIT license.

"""

"""

import pyautogui
import time

def printMouseCoordinates():
    """docstring for pr"""
    x,y = pyautogui.position()
    print("mouse: x: "+ str(x).rjust(4) + "; y: " + str(y).rjust(4))

def clickGoogleCalendarBrowserTab():
    """docstring for clickGoogleCalendarBrowserTab"""
    x,y = (69,50)
    print("Clicking GoogleCalendar webbrowser tab in x:" + str(x).rjust(4), "; y: " + str(y).rjust(4))
    pyautogui.click(x,y)

def scrollDown():
    """docstring for scrollDow"""
    print ("Scrolling down")
    pyautogui.scroll(200)

def scrollDown():
    """docstring for scrollDow"""
    print ("Scrolling down")
    pyautogui.scroll(200)
    

if __name__ == "__main__":    
    print("Press Ctrl-C to quit");
    while True:
        printMouseCoordinates()
        #clickGoogleCalendarBrowserTab();
        #scrollDown();
        time.sleep(1)
