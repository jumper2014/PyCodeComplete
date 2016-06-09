# coding=utf-8
# 日期数据

import datetime

today = datetime.date.today()
print today
print 'ctime:', today.ctime()
print 'tuple:', today.timetuple()  #返回日期对应的time.struct_time对象；
print 'ordinal:', today.toordinal() # 返回日期对应的Gregorian Calendar日期；罗马教皇格利高里的
print 'Year:', today.year
print 'Mon :', today.month
print 'Day :', today.day
