# coding=utf-8
# 计算昨天和明天的日期

import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(yesterday, today, tomorrow)