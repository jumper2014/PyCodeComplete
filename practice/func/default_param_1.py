#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


def f1(a, L=[]):
    L.append(a)
    return L


print(f1(1))
print(f1(2))
print(f1(3))


def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f2(1))
print(f2(2))
print(f2(3))
