# coding=utf-8
# 格式化字符串

import sys

user = 'BBB'

email = 'BBB@example.com'
full_name = 'BBB Frist'
user_spec = str.format("\
User: %s  \n\
Email: %s  \n\
Update:  \n\
Access:  \n\
FullName: %s \n\
Password:  \n\
" % (user, email, full_name))

print user_spec


str1 = "{key}={value}".format(key="a", value=10)
print str1

str1 = "{0.platform}".format(sys)
print str1

str1 = "{0[a]}".format(dict(a=10, b=20))
print str1

str1 = "{0[5]}".format(range(10))
print str1

str1 = "My name is {0} :-{{}}".format('Fred') # 真的想显示{}
print str1
