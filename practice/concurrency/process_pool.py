#!/usr/bin/env python
# coding=utf-8
# 进程池实例
# apply 单个任务同步
# apply_async 单个任务异步
# map 多个任务同步
# map_async 多个任务异步

import time
from multiprocessing import Pool            # 多进程
# from multiprocessing.dummy import Pool      # 多线程


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
    pool.apply_async(task_short, args=(11, ))

    # 同步任务
    pool.map(task_long, range(10))
    print("main process")