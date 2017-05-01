# coding=utf-8

from threading import Timer
import time

num = 0
datas = range(100)


def handle_list():
    global num
    print "-------", datas[num]
    t = Timer(1, handle_list)
    t.start()
    num += 1


def wait_to_end():
    i = 0
    while i < 10000:
        print i
        i += 1
        time.sleep(0.1)