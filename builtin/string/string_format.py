# coding=utf-8
# 格式化字符串

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
