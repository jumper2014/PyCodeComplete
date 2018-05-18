#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

if __name__ == '__main__':
    # 带宽，丢包，延迟
    parameters = [
        ["1M", "3M", "5M", "10M"],
        ["1%", "5%", "10%", "15%"],
        ["0ms", "50ms", "100ms", "200ms"]
    ]

    pairwise = all_pairs(parameters)
    for i, v in enumerate(pairwise):
        print("%i:\t%s" %(i, str(v)))

    """
    0:	['1M', '1%', '0ms']
    1:	['3M', '5%', '0ms']
    2:	['5M', '10%', '0ms']
    3:	['10M', '15%', '0ms']
    4:	['10M', '10%', '50ms']
    5:	['5M', '5%', '50ms']
    6:	['3M', '1%', '50ms']
    7:	['1M', '15%', '50ms']
    8:	['1M', '10%', '100ms']
    9:	['3M', '15%', '100ms']
    10:	['5M', '1%', '100ms']
    11:	['10M', '5%', '100ms']
    12:	['10M', '1%', '200ms']
    13:	['5M', '15%', '200ms']
    14:	['3M', '10%', '200ms']
    15:	['1M', '5%', '200ms']
    """