# coding=utf-8
# Second, Millisecond(毫秒), Microsecond(微秒)

import time
import datetime

print(time.time())       # 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
# 1493019531.63

print(datetime.datetime.now().microsecond)        # 获取当前时间的微秒数
# 630000