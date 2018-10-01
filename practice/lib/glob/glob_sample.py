#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import glob

if __name__ == '__main__':
    files = glob.glob(pathname='../../../*.py', recursive=True)
    print(files)