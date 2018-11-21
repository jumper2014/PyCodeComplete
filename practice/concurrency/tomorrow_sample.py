#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


import time
import requests
from tomorrow import threads

urls = [
    'http://www.baidu.com',
    'http://www.163.com',
    'http://www.bilibili.com',
    'http://www.jd.com',
    'http://www.12306.com',
    'http://www.sohu.com',
    'http://www.taobao.com'
]


@threads(10)
def download(url):
    return requests.get(url)


if __name__ == "__main__":
    import time

    start = time.time()
    responses = [download(url) for url in urls]
    html = [response.text for response in responses]
    end = time.time()
    print("Time: %f seconds" % (end - start))
    # Time: 0.171315 seconds