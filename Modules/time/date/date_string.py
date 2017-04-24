# coding=utf-8
# 日期字符串

import time

ISOTIMEFORMAT='%Y-%m-%d %X'

# 1970/1/1 00:00:00
print time.time()

# 当前时区
current = time.localtime()
# strfmtime格式化
print time.strftime("%Y%m%d%H%M%S", current)

# 0 时区 UTC时区
current = time.gmtime()
print time.strftime(ISOTIMEFORMAT, current)

# 查看时区 -28800=8*3600
print time.timezone

# 将一个时间戳（默认当前时间）转换成时间字符串
time_str = time.time()
print time.ctime(time_str)
print time.ctime()