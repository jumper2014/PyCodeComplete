#!/usr/bin/env python
# coding=utf-8
# 演示守护线程
# 守护线程(thread-0)会随着主线程退出而退出
# 主线程需要等待所有非守护线程(thread-1)退出才退出

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


