# coding=utf-8
# 在使用kwargs参数中如果获得键值对

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

greet_me(name="yasoob", age=30)

