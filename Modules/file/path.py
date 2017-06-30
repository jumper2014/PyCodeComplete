# coding=utf-8
import inspect
import os
import sys


def get_root_path():
    file_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
    print(file_path)
    parent_path = os.path.dirname(file_path)
    parent_path = os.path.dirname(parent_path)
    parent_path = os.path.dirname(parent_path)
    print(parent_path)
    return parent_path


if __name__ == "__main__":
    get_root_path()
