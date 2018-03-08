### 常见的误解
Python初学者会有一个误解，那就是设置线程为Daemon，主线程退出后，子线程仍运行直到任务结束。其实，这是不对的。

在维基百科是这样定义守护程序的
> In multitasking computer operating systems, a daemon (/ˈdiːmən/ or /ˈdeɪmən/)is a computer program that runs as a background process, rather than being under the direct control of an interactive user.

可见，这里并没有说到守护线程是否会跟随主线程一起退出，仅仅提到了在后台运行，并且不和用户直接交互。

### Python里的守护线程
> A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property.

要点：线程可以通过setDaemon(True)被设置为守护线程，当仅有守护线程运行时，主程序才能退出。

### 为何要设置守护线程
> Daemons are only useful when the main program is running, and it's okay to kill them off once the other non-daemon threads have exited. Without daemon threads, we have to keep track of them, and tell them to exit, before our program can completely quit. By setting them as daemon threads, we can let them run and forget about them, and when our program quits, any daemon threads are killed automatically.

1. 主线程活着的时候，守护线程才会存活。主线程结束后，守护线程会自动被杀死结束运行。
2. 主线程需等所有非守护线程退出后才会退出，如果想要结束非守护线程，我们必须手动找出非守护线程将其杀死。

### 总结
- 如果需要子线程随主线程一同退出-设置它为守护线程。
- 如果需要子线程运行结束后，主线程才能退出-设置子线程为非守护线程。

### 实例
主线程启动两个子线程：
- 子线程0-守护线程，运行10秒退出
- 子线程1-非守护线程，运行1秒退出。

根据我们上面的总结，我们会知道：
- 主线程启动完子线程，等待所有非守护线程运行
- 非守护子线程1运行1秒退出
- 此时没有非守护线程运行，主线程退出
- 子线程0虽然任务还未完成，但是它是守护线程，会紧跟主线程退出。

```
import time
import threading


def sub(num):
    if i % 2 == 0:
        time.sleep(10)
    else:
        time.sleep(1)
    print("thread-{0}: done\n".format(num))


if __name__ == "__main__":
    for i in range(2):
        t = threading.Thread(target=sub, args=(i, ))
        if i % 2 == 0:
            t.setDaemon(True)
        t.start()
        print("thread-{0} started".format(i))
```
运行结果如下：
```
thread-0 started
thread-1 started
thread-1: done
```

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/blob/master/practice/concurrency/20180113/threading_daemon.py)