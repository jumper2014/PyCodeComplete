#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import requests
import requests_cache
import time

if __name__ == '__main__':
    requests_cache.install_cache(expire_after=300)
    start = time.time()
    for i in range(10):
        response = requests.get('http://httpbin.org/delay/1')
        print(response.content)
    print("cost time: {}".format(time.time()-start))