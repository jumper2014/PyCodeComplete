#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import json_tools

if __name__ == '__main__':
    a = {'left':1, "right":{"a": [1, 2, {"b":"x", "a":1}]}}
    b = {'right':{"a":[1, 2, {"a":1, "b":'x'}]}, "left":1}

    result = json_tools.diff(a, b)
    print(result)