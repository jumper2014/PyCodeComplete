#!/usr/bin/env python
# coding=utf-8


class UserMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['register'] = True
        return type.__new__(cls, name, bases, attrs)


class User(object):
    __metaclass__ = UserMetaclass


if __name__ == '__main__':
    user = User()
    print(user.register)