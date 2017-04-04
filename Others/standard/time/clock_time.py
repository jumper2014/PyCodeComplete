# coding=utf-8
# 计算CPU用时和间隔时间

import time


def procedure():
    time.sleep(2.5)

# Return the CPU time or real time since the start of the process or since
#     the first call to clock()

# measure process time
t0 = time.clock()
procedure()
print time.clock() - t0, "seconds process time"

# measure wall time
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"