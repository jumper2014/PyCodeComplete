#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import unittest


class Count(object):
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b


class TestCount(unittest.TestCase):
    def setUp(self):
        print("Test Start")

    def tearDown(self):
        print("Test End")

    def test_add1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(3, 3)
        self.assertEqual(j.add(), 5)


if __name__ == "__main__":
    # 1. 新建测试套件
    suite = unittest.TestSuite()
    # 2. 将用例加入测试套件
    suite.addTest(TestCount("test_add1"))
    suite.addTest(TestCount("test_add2"))
    # 3. 新建TestRunner
    runner = unittest.TextTestRunner()
    # 4. 用TestRunner来执行TestSuite
    runner.run(suite)