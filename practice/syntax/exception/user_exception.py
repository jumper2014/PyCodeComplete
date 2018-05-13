#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


class VerifyException(Exception):
    def __init__(self, message):
        super().__init__(self)
        self.message = message

    def __str__(self):
        return self.message


if __name__ == '__main__':
    user_age = -1
    try:
        if user_age < 0:
            raise VerifyException('User age is negative')
    except Exception as e:
        print(e.message)
