# coding=utf-8
# 在Python中使用printf

import sys


def printf(fmt, *args):
    sys.stdout.write(fmt % args)

printf("%d %s", 10*100, "python")