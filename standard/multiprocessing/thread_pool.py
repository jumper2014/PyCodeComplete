# coding=utf-8
# 一行代码实现多线程/多进程

import urllib2
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.163.com',
    'http://www.baidu.com',
    'http://www.sina.com.cn'
]

pool = ThreadPool(4)
results = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()
