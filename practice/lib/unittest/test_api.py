#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import unittest
import requests
from unittest import TestCase
from unittest.mock import patch


class User(object):
    def get_user_info(uid):
        resp = requests.get("http://api.server.com/user/{0}".format(uid))
        return resp.json()


class TestUserInfo(TestCase):
    @patch('__main__.User')
    def test_user_name(self, MockUser):
        user = MockUser()
        user.get_user_info.return_value = {
            "user_id": 1,
            "name": "python",
            "age": 20
        }
        resp = user.get_user_info(1)
        self.assertEqual(resp.get("name"), "python")
        self.assertEqual(resp.get("age"), 20)


if __name__ == '__main__':
    unittest.main()