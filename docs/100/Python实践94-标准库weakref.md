### 弱引用
- 弱引用，与强引用相对，是指不能确保其引用的对象不会被垃圾回收器回收的引用。一个对象若只被弱引用所引用，则可能在任何时刻被回收。弱引用的主要作用就是减少循环引用，减少内存中不必要的对象存在的数量。

### weakref的适用场合
- Python 自动进行内存管理（对大多数的对象进行引用计数和垃圾回收—— 垃圾回收 ——以循环利用）在最后一个引用消失后，内存会很快释放。
- 这个工作方式对大多数应用程序工作良好，但是偶尔会需要跟踪对象来做一些事。不幸的是，仅仅为跟踪它们创建引用也会使其长期存在。 weakref 模块提供了不用创建引用的跟踪对象工具，一旦对象不再存在，它自动从弱引用表上删除并触发回调。

### 举个栗子
```
import gc
import weakref
import sys


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


if __name__ == '__main__':
    ##############################
    # 强引用
    ##############################
    a = A(88)
    print(sys.getrefcount(a))  # 2
    d = dict()
    d['primary'] = a
    print(d['primary'])         # 88
    print(sys.getrefcount(a))   # 3

    del a
    gc.collect()            # 立即进行垃圾回收
    print(d['primary'])     # 88 依然存在

    ##############################
    # 弱引用
    ##############################
    a = A(88)
    print(sys.getrefcount(a))   # 2
    d = weakref.WeakValueDictionary()
    d['primary'] = a            # 这里是弱引用
    print(d['primary'])         # 88
    print(sys.getrefcount(a))   # 2

    del a
    gc.collect()            # 立即进行垃圾回收
    print(d['primary'])  # 已经不存在，抛出KeyError异常
```