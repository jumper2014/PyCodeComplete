#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
import time
from itertools import count
from hashlib import md5


if __name__ == "__main__":
    start = time.time()
    msg = 'randomstring'
    for i in count():
        hashid = md5(msg + str(i)).hexdigest()
        if hashid.startswith('0000000'):
            print i, hashid
            break
    print('Time: {0}'.format(time.time() - start))