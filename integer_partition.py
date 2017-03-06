#!/usr/bin/env python

#============================================#
#
# Author: penn - penn201500@gmail.com
# Last modified: 2017-03-05 15:42
# Filename: integer_partition.py
# Description:
#
#===========================================#


def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
          answer.add(tuple(sorted((x, ) + y)))
    return answer

if __name__ == '__main__':
	print partition(5)
