# coding=utf-8
# 寻找上一个星期五

import datetime, calendar
lastFriday = datetime.date.today()
while lastFriday.weekday() != calendar.FRIDAY:
    lastFriday -= datetime.date.resolution
print lastFriday.strftime('%d-%b-%Y')

# 另一种方法
lastFriday = datetime.date.today()
oneday = datetime.timedelta(days=1)
while lastFriday.weekday() != calendar.FRIDAY:
    lastFriday -= oneday
print lastFriday.strftime('%d-%b-%Y')