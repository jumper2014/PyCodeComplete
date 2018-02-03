#!/usr/bin/env python
# coding=utf-8

from flask import Flask
app = Flask(__name__)


def make_func(i):
    def func():
        return 'this is {0}'.format(i)
    return func


if __name__ == '__main__':
    funcs = map(make_func, range(2))
    print(funcs)
    for i in range(2):
        app.add_url_rule('/test{0}'.format(i), endpoint='{0}'.format(i), view_func=funcs[i])

    app.run(host='0.0.0.0', port=8080)
