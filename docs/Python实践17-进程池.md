### 多进程的优势
- 尽管Python中的线程是OS原生的（它们不是被模拟出来的，它们是真实的操作系统线程），它们被全局解释器锁(GIL)所束缚，所以同一时刻只有一个线程可以和Python对象交互。
- 通过使用多进程，我们并行运行一定数量的Python解释器，每一个进程都有私有的内存空间，有自己的GIL，并且每一个都穿行运行（所有没有GIL之间的竞争），这是在Python中提升CPU密集型任务速度的最简单方式。

### 为什么要用进程池
如果每个任务使用一个进程，每处理一个任务都会伴随着一个进程的创建、运行、销毁，如果进程的运行时间越短，创建和销毁的时间所占的比重就越大，显然，我们应该尽量避免创建和销毁进程本身的额外开销，提高进程的运行效率。我们可以用进程池来减少进程的创建和开销，提高进程对象的复用。

### Python的进程池
- Python中已经实现了一个功能强大的进程池（multiprocessing.Pool），可以很方便地创建进程池对象。
- 要创建进程池对象，需要调用Pool函数，函数的声明如下：
> Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None)

1. processes表示工作进程的个数，默认为None，表示worker进程数为cpu_count()
2. initializer表示工作进程start时调用的初始化函数，initargs表示initializer函数的参数，如果initializer不为None，在每个工作进程start之前会调用initializer(*initargs)
3. maxtaskperchild表示每个工作进程在退出/被其他新的进程替代前，需要完成的工作任务数，默认为None，表示工作进程存活时间与pool相同，即不会自动退出/被替换。
4. 函数返回一个进程池（Pool）对象

### 分配任务和同步异步
Pool对象有下面几个主要的方法用于将任务分配到进程池中去，它们分别是
- apply 单个任务同步
- apply_async 单个任务异步
- map 多个任务同步
- map_async 多个任务异步
其中不带async的方法都会阻塞到任务完成，才会继续运行其后的代码。

下面是一个例子：
```
def task_short(num):
    time.sleep(3)
    print("I am task: {0}\n".format(num))


def task_long(num):
    while True:
        print("I am task: {0}\n".format(num))
        time.sleep(1)

if __name__ == "__main__":
    pool = Pool(processes=5)

    # 异步任务
    pool.apply_async(task_short, args=(10, ))

    # 同步任务
    pool.map(task_long, range(10))
    print("main process")
```
该例子创建了一个有5个worker的进程池，并先将1个任务task_short异步地加入进程池中运行，然后又将10个任务task_long同步地加入进程池中。  
由于task_short需要3秒才能执行完，所以一开始task_long任务可用的worker进程只有4个。3秒后task_short完成，进程池会自动再加载1个task_long任务交给刚刚空闲的那个worker进程执行。  
由于task_long任务永远不会结束，所以其他剩余的任务5到9都没有机会执行。

### 局限
通过上面的例子，我们发现进程池不适合执行那些永远不会完成的任务，比如后台服务，因为没有worker进程执行完成的话，其他的进程就永远不会被执行。

### multiprocessing.dummy
multiprocessing.dummy里面也有一个Pool对象，它其实就是线程的封装，使用起来和multiprocessing的Pool非常类似。  
因为多进程适合计算密集的多任务，多线程适合IO密集的多任务，所以在代码里面使用下面两句，需要的时候注释掉其中之一，可以做到进程模型和线程模型的一键切换。  
如果你不知道自己的程序是计算密集的还是IO密集的，就切换下试试，哪个性能表现好，就用哪个。
> from multiprocessing.dummy import Pool      # 多线程  
> from multiprocessing import Pool            # 多进程

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/tree/master/practice/concurrency/20180116)
