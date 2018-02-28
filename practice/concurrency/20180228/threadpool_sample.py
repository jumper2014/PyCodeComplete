#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import threadpool
import urllib2
import time


def visit_url(url):
    response = urllib2.urlopen(url)
    page = response.read()
    print(page.decode('utf-8'))

if __name__ == "__main__":
    start = time.time()
    pool_size = 20                  # 线程池大小 20
    # 创建需要处理的URL序列
    urls = ['http://api.bilibili.com/x/web-interface/archive/stat?aid={0}'.format(i) for i in range(1, 1001)]

    # 基本结构
    pool = threadpool.ThreadPool(pool_size)
    requests = threadpool.makeRequests(visit_url, urls)
    [pool.putRequest(req) for req in requests]
    pool.wait()

    # 完成后退出
    pool.dismissWorkers(pool_size, do_join=True)
    print('TIME: ', time.time() - start)
