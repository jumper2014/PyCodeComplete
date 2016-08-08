# coding=utf-8
"""
演示使用defaultdict提供默认值

defaultdict可以接受一个函数作为参数
collections.defaultdict会返回一个类似dictionary的对象，
注意是类似的对象，不是完全一样的对象。
这个defaultdict和dict类，几乎是一样的，除了它重载了一个方法和增加了一个可写的实例变量。

如果default_factory不是None, 这个default_factory将以一个无参数的形式被调用，提供一个默认值给___missing__方法的key。
这个默认值将作为key插入到数据字典里，然后返回。

"""
import collections

def default_factory():
    return 'default value'


if __name__ == "__main__":
    d = collections.defaultdict(default_factory, foo='bar')
    print 'd:', d
    print 'foo = > ', d['foo']
    print 'bar = > ', d['bar']