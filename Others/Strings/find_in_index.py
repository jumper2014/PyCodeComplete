#!/usr/bin/env python3
# coding=utf-8
# 在字符串中查找字串

if 'hello world,hello'.find('world') != -1:
    print('find')

if 'world' in 'hello world,hello':
    print('find')

if 'hello world,hello'.index('world'):
    print('find')

try:
    if 'hello world, hello'.index('world') >= 0:
        print('find')
except:
        pass
