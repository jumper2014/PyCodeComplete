# coding=utf-8
# 返回一个lambda函数的函数

def action(x):
    return (lambda y: x + y)

act = action(2)

print act

print act(98)