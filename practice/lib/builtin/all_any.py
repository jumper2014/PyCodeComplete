#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

if __name__ == "__main__":
    elements = [False, False, True]
    print(all(elements))  # False
    print(any(elements))  # True

    elements = []
    print(all(elements))  # True
    print(any(elements))  # False
