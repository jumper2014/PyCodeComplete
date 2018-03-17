#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import json
if __name__ == '__main__':
    user = {'id': 1, 'name': 'python', 'age': 30}
    print(type(user))  # < type 'dict' >
    print(user)  # {'age': 30, 'id': 1, 'name': 'python'}

    json.dump(user, open('user.json', 'w'))

    fp = open('user.json', 'r')
    user2 = json.load(fp)
    print(type(user2))  # <type 'dict'>
    print(user2)  # {u'age': 30, u'id': 1, u'name': u'python'}