#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import demjson

if __name__ == '__main__':
    # From Python to JSON
    print(demjson.encode(['one', 42, True, None]))
    # '["one",42,true,null]'

    # From JSON to Python
    print(demjson.decode('["one",42,true,null]'))
    # ['one', 42, True, None]

    # 处理不规范的JSON字符串
    print(demjson.decode('{name: "python", age: 42}'))
    # {u'age': 42, u'name': u'python'}

    # 严格模式时，不规范的json串会报异常
    print(demjson.decode('{name: "python", age: 42}', strict=True))
    # demjson.JSONDecodeError
