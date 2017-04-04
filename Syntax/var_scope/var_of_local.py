# coding=utf-8

# 局部作用域
# name的作用域也只是在函数内部，外部依然无法进行调用


def func():
    name = "lzl"


func()  # 执行函数
print(name)
