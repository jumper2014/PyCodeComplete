#!/usr/bin/env python
import yappi
import threading

from samples.yappi.funcs import consumer_time

def aggregate(func, stats):
    fname = "%s.profile" % (func.__name__)
    try:
        stats.add(fname)
    except IOError:
        pass
    stats.save(fname)


# @yappi.profile(return_callback=aggregate)
def sum(x, y):
    consumer_time()
    return x + y


import yappi
if __name__ == "__main__":
    # yappi.set_clock_type("wall")
    yappi.set_clock_type("cpu")
    yappi.start()
    for i in range(10):
        t = threading.Thread(target=sum, args=(100, i,), name="hello"+str(i))
        t.start()
    main_thread = threading.currentThread()

    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    yappi.get_func_stats().print_all(columns= {0:("name",50), 1:("ncall", 15),
                    2:("tsub", 18), 3: ("ttot", 18), 4:("tavg",18)})
    yappi.get_thread_stats().print_all()
