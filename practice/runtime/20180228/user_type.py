#!/usr/bin/env python
# coding=utf-8

if __name__ == '__main__':
    User = type('User', (object,), dict(register=True))  # 创建User class
    user = User()
    print(user.register)