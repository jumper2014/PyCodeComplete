# coding=utf
# 用户自定义的异常类

#Exceptions should typically be derived from the Exception class, either directly or 
#indirectly. For example:

class MyError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
 
try:
     raise MyError(2*2)
except MyError, e:
     print 'My exception occurred, value:', e.value
 