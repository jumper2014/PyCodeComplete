#!/usr/bin/env python
# coding=utf-8


import time
import requests
from concurrent.futures import ProcessPoolExecutor


def visit_url(url):
    response = requests.request('GET', url)
    return response.content


if __name__ == '__main__':

    start = time.time()
    # 创建需要处理的URL序列
    urls = ['http://api.bilibili.com/x/web-interface/archive/stat?aid={0}'.format(i) for i in range(1, 1001)]

    with ProcessPoolExecutor(max_workers=20) as executor:
        # result = executor.map(visit_url, urls)
        for num, result in zip(range(1, 1001), executor.map(visit_url, urls)):
            print('video ({}) = {}'.format(num, result))

    print 'COST: {}'.format(time.time() - start)