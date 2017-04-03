# coding=utf-8

# 可以看到, 一般递归, 每一级递归都需要调用函数, 会创建新的栈,
# 随着递归深度的增加, 创建的栈越来越多, 造成爆栈


def normal_recursion(n):
    if n == 1:
        return 1
    else:
        return n + normal_recursion(n-1)

print(normal_recursion(900))