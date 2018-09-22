#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


def decorator(cls):
    class Wrapper(object):
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print('Getting the {} of {}'.format(name, self.wrapped))
            return getattr(self.wrapped, name)

    return Wrapper

@decorator
class C(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    x = C(1,2)
    print(x.x)