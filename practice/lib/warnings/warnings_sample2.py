#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import warnings


def function_with_warning():
    warnings.warn('This is a warning!')


if __name__ == '__main__':
    function_with_warning()
    function_with_warning()
    function_with_warning()