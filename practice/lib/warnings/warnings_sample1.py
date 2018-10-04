#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import warnings
if __name__ == '__main__':

    # 凡是UserWarning都转换为的异常
    warnings.simplefilter(action='error', category=UserWarning)

    print('Before the warning')
    warnings.warn('This is a warning message')
    print('After the warning')