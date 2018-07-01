### 背景
- 之前我们提到内置的multiprocessing模块里面也有线程池，那么它和我们常常在代码里面看到的threadpool模块有什么区别呢？
- threadpool模块是一个很老的实现python线程池的模块,是第三方库
- threadpool官方说它已经被废弃了，虽然它在Python2和Python3里面还能用。
- 官方建议用multiprocessing和Python3里面的asyncio替代它。

### 代码结构
- 既然已经被官方认证为废弃的模块，那么为什么还有人喜欢用它呢？原因是易于理解。
- 下面我们看一个典型的代码结构
```
from threadpool import *
pool = ThreadPool(poolsize) 
requests = makeRequests(some_callable, list_of_args, callback) 
[pool.putRequest(req) for req in requests] 
pool.wait()
```
- 第2行定义了一个线程池，表示最多可以创建poolsize这么多线程；
- 第3行是调用makeRequests创建了要开启多线程的函数，以及函数相关参数和回调函数，其中回调函数可以不写，default是无，也就是说makeRequests只需要2个参数就可以运行；
- 第4行用法比较奇怪，是将所有要运行多线程的请求扔进线程池。
- 第5行是等待所有的线程完成工作后退出。

### 用threadpool来爬取哔哩哔哩
- 我们下面用threadpool来爬取bilibili.com网站的视频基本信息数据，即某视频有多少人看过等信息
- B站的视频该信息的查询接口为http://api.bilibili.com/x/web-interface/archive/stat?aid={id}
- 代码如下
```
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
```

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/PyCodeComplete/tree/master/practice/concurrency/20180228)