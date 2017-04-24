# coding=utf-8
# 线程池的例子

import urllib2
import os
import time
import threadpool


def download_file(url):
    print "begin download", url
    urlhandler = urllib2.urlopen(url)
    fname = os.path.basename(url) + ".html"
    with open(fname, "wb") as f:
        while True:
            chunk = urlhandler.read(1024)
            if not chunk:
                break
            f.write(chunk)

urls = ["http://www.baidu.com", "http://www.163.com", "http://www.chouti.com"]
pool_size = 2
pool = threadpool.ThreadPool(pool_size)
requests = threadpool.makeRequests(download_file, urls)

[pool.putRequest(req) for req in requests]

print "putting request to pool"
pool.putRequest(threadpool.WorkRequest(download_file, args=["http://www.sohu.com",]))
pool.putRequest(threadpool.WorkRequest(download_file, args=["http://www.qq.com",]))
pool.poll()
pool.wait()
print "destroy all threads before exit"
pool.dismissWorkers(pool_size, do_join=True)  # 完成后退出

