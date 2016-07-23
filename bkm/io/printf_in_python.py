# coding=utf-8
# 在Python中使用printf

import sys


def printf(format, *args):
    sys.stdout.write(format % args)

printf("%d %s", 10*100, "python")