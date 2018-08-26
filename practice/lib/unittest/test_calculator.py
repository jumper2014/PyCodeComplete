#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import unittest
import time
from unittest import TestCase
from unittest.mock import patch


def sum(a, b):
    time.sleep(100)  # long running process
    return a + b


class TestCalculator(TestCase):
    @patch('__main__.sum', return_value=5)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
