#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import time
import threading
from urllib import request


def visit_url(url):
    response = request.urlopen(url)
    page = response.read()
    print(page.decode('utf-8'))

now = lambda: time.time()

if __name__ == "__main__":
    threads = list()
    start = now()
    for i in range(1, 1001):
        t = threading.Thread(target=visit_url, args=('http://api.bilibili.com/x/web-interface/archive/stat?aid={0}'.format(i),))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('TIME: ', now() - start)