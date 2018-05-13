#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import unittest


def setUpModule():
    print("setUpModule >>>")


def tearDownModule():
    print("tearDownModule >>>")


class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass for Test1 >>")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass for Test1 >>")

    def setUp(self):
        print("setUp for Test1 >")

    def tearDown(self):
        print("tearDown for Test1 >")

    def testCase1(self):
        print("testCase1 for Test1")

    def testCase2(self):
        print("testCase2 for Test1")


class Test2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass for Test2 >>")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass for Test2 >>")

    def setUp(self):
        print("setUp for Test2 >")

    def tearDown(self):
        print("tearDown for Test2 >")

    def testCase1(self):
        print("testCase1 for Test2")

    def testCase2(self):
        print("testCase2 for Test2")


if __name__ == "__main__":
    unittest.main()
