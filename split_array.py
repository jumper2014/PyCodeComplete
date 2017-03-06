#!/usr/bin/env python

#============================================#
#
# Author: penn - penn201500@gmail.com
# Last modified: 2017-03-03 12:46
# Filename: split_array.py
# Description:
#
#===========================================#
def split_array(l,n):
    i = 0
    if len(l) == 0:
        print 'wrong'
    else:
        while i<=len(l):
            yield l[i:i+n]
            i += n

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7]
    for i in split_array(l,2):
        print i
