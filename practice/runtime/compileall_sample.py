#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


if __name__ == '__main__':
    import compileall
    compileall.compile_dir('.', force=True)