# coding=utf-8

"""
其实defaultdict 就是一个字典，只不过python自动的为它的键赋了一个初始值。
这也就是说，你不显示的为字典的键赋初值python不会报错，看下实际例子。

比如你想计算频率

frequencies = {}
for word in wordlist:
    frequencies[word] += 1
python会抛出一个KeyError 异常，因为字典索引之前必须初始化，可以用下面的方法解决
"""

wordlist = ["hello", "python"]
frequencies = dict()
for word in wordlist:
    try:
        frequencies[word] += 1
    except KeyError:
        frequencies[word] = 1
print frequencies

frequencies = dict()
for word in wordlist:
    if word in frequencies:
        frequencies[word] += 1
    else:
        frequencies[word] = 1

print frequencies

"""
当然，collections.defaultdict也可以轻松的解决这个问题
"""

from collections import defaultdict

frequencies = defaultdict(int) #传入int()函数来初始化
for word in wordlist:
    frequencies[word] += 1

print frequencies
"""
collections.defaultdict可以接受一个函数作为参数来初始化。什么意思呢，看上面的例子，我们想要frequencies[word]初始化为0，
这时就可以用一个int()函数作为参数出给defaultdict，我们不带参数调用int()，int()就会返回一个0值
"""