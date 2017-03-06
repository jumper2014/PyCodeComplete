# coding=utf-8
# 函数返回另一个函数


def knights():
    title = 'sir'
    action = (lambda x: title + " " + x)
    return action

act = knights()
print act('robin')
