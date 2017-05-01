# coding=utf-8

import threading
from setting_parallel import *


if __name__ == '__main__':
    t = Timer(1, handle_list)
    t.start()
    index = 1000

    t = threading.Thread(target=wait_to_end)
    t.start()

    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()

    print "end"
