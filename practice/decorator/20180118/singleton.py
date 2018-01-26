#!/usr/bin/env python
# coding=utf-8


def singleton(cls):
    instances = dict()

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton



if __name__ == "__main__":
    pass