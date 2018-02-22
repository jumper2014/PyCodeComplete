#!/usr/bin/env python
# coding=utf-8

import os.path
import pathlib

# 检查给定路径是否是文件，能够区分文件和目录
print(os.path.isfile('/etc/passwd'))    # True
print(os.path.isfile('/etc'))           # False
print(os.path.isfile('/does/not/exists'))   # False

# 检查给定路径是否存在，无法能够区分文件和目录
print(os.path.exists('/etc/passwd'))    # True
print(os.path.exists('/etc'))           # True
print(os.path.exists('/does/not/exists'))   # False

# Python2需要安装pathlib, Python3中pathlib是内置模块，无需安装
path = pathlib.Path("/etc/passwd")
print(path.exists())                    # True
print(path.is_file())                   # True
print(path.is_dir())                    # False

