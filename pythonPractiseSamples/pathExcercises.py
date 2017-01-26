#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
import os

class TestPathMethods(unittest.TestCase):

    def setUp(self):
        self.sampleAbsolutePath = "/home/user/test/project"
        self.relativePath = "../test/project"

    def test_abspath(self):
        self.assertEqual(os.path.abspath(self.relativePath), "/home/damian/other/practiseSamples/test/project");

    def test_basename(self):
        self.assertEqual(os.path.basename(self.sampleAbsolutePath), "project");

    def test_exists(self):
        self.assertEqual(os.path.exists(self.sampleAbsolutePath), False);

    def test_expanduser(self):
        self.assertEqual(os.path.expanduser("~/dir"), "/home/damian/dir");

    def test_isabs(self):
        self.assertEqual(os.path.isabs("./dir"), False);
        self.assertEqual(os.path.isabs("~/dir"), False);
        self.assertEqual(os.path.isabs("/home/damian/dir"), True);

    def test_isfile(self):
        self.assertEqual(os.path.isfile("/etc"), False);
        self.assertEqual(os.path.isfile("/etc/hosts"), True);

    def test_isdir(self):
        self.assertEqual(os.path.isdir("/etc"), True);
        self.assertEqual(os.path.isdir("/etc/hosts"), False);

    def test_join(self):
        self.assertEqual(os.path.join("/etc", "crontab"), "/etc/crontab");

if __name__ == "__main__": 
    print ("running unittests for path")
    unittest.main();
