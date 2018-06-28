#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import yagmail

if __name__ == '__main__':
    yag = yagmail.SMTP(user="user1@163.com", password="user1password", host='smtp.163.com')

    contents = ['This is the body, and here is just text https://zhuanlan.zhihu.com/python2018',
                'You can find an file attached.', '/tmp/sample.png']

    yag.send(to='user2@hotmail.com',
             subject='yagmail sample',
             contents=contents)
