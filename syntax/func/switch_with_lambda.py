# coding=utf-8
# 使用lambda模拟switch

# Python has no switch keyword
# Here we simulate switch with lambda

def a(s):
    print s


def switch(ch):
    try:
        {
            '1': lambda: a("one"),
            '2': lambda: a("two"),
            '3': lambda: a("three")

        }[ch]()
    except KeyError:
        a("key not found")


switch("1")
switch("a")
