# coding=utf-8
# Timers通过调用它们的start()方法作为线程启动。
# timer可以通过调用cancel()方法（在它的动作开始之前）停止。
# timer在执行它的动作之前等待的时间间隔可能与用户指定的时间间隔不完全相同。

from threading import Timer

def fun():
    print "hello, world"

if __name__=='__main__':
    t = Timer(5.0, fun)
    t.start() # 开始执行线程，但是不会打印"hello, world"
    t.cancel() # 因为cancel取消了线程的执行，所以fun()函数不会被执行