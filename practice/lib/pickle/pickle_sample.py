#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import pickle


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name + "_" + str(self.age))


# 序列化到文件
user = User("Python", 20)
user.show()
f = open('user.pkl', 'wb')
pickle.dump(user, f)
f.close()

# 反序列化到内存
f = open('user.pkl', 'rb')
user1 = pickle.load(f)
f.close()
user1.show()
