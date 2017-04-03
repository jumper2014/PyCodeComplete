# coding=utf-8

# 尾递归基于函数的尾调用, 每一级调用直接返回函数的返回值更新调用栈,
# 而不用创建新的调用栈, 类似迭代的实现, 时间和空间上均优化了一般递归!


def tail_recursion(n, total=0):
    if n == 0:
        return total
    else:
        return tail_recursion(n-1, total+n)

print(tail_recursion(900))