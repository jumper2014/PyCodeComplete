# coding=utf-8


# python          json
# dict            object
# list, tuple     array
# str, unicode    string
# int, float, long# number
# True              true
# False             false
# None              null

import json

# 转成json
obj = [[1, 2, 3], 123, 123.123, 'abc', {'key1': (1, 2, 3), 'key2': (4, 5, 6)}]

encoded_json = json.dumps(obj)
print repr(obj)
print encoded_json

# json                  python
# object                dict
# array                 list
# string                unicode
# number(int)           int, long
# number(real)          float
# true                  True
# false                 False
# null                  None

# 转成python数据结构
decode_json = json.loads(encoded_json)
print type(decode_json)
print decode_json[4]['key1']
print decode_json
