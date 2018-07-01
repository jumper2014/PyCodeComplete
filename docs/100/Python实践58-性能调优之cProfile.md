### cProfile简介
- cProfile是一个标准库内建的分析工具。它hook进CPython的虚拟机来测量其每一个函数运行所花费的时间。这一技术会引入一个巨大的开销，但你会获得更多的信息。有时这些额外的信息会给你的代码带来令人惊讶的发现。
- cProfile是标准库内建的三个分析工具之一，另外两个是hotshot和profile。
- hotshot还处于实验阶段，profile则是原始的纯Python分析器。cProfile具有跟profile一样的接口，且是默认的分析工具。
- 永远不要忽视靠直觉进行的性能分析（虽然你一定会犯错！）。在分析前先进行假设是绝对值得的，因为这样可以帮助你学习如何定位你代码中可能有问题的地方，而且你应该始终用证据来证明你的选择。

### 使用cProfile
- 通过命令行直接profile你的Python程序：python -m cProfile foo.py
- 输出的字段含义如下：
```
ncalls：表示函数调用的次数；
tottime：表示指定函数的总的运行时间，除掉函数中调用子函数的运行时间；
percall：（第一个percall）等于 tottime/ncalls；
cumtime：表示该函数及其所有子函数的调用运行的时间，即函数开始调用到返回的时间；
percall：（第二个percall）即函数运行一次的平均时间，等于 cumtime/ncalls；
filename:lineno(function)：每个函数调用的具体信息；
```

### 一个例子
- 定义一个被引用的模块bar
```
def bar():
    result = 0
    for i in range(1000000):
        result += i
    return result
```

- 定义一个导入bar的主程序foo.py
```
from bar import bar


def foo():
    result = 0
    for i in range(100000):
        result += i
    for i in range(5):
        bar()
    return result


if __name__ == '__main__':
    foo()
```

- 运行cProfile来分析foo.py的性能
```
python -m cProfile  foo.py
         16 function calls in 0.234 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 bar.py:6(<module>)
        5    0.181    0.036    0.227    0.045 bar.py:6(bar)
        1    0.000    0.000    0.234    0.234 foo.py:5(<module>)
        1    0.003    0.003    0.233    0.233 foo.py:8(foo)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        7    0.049    0.007    0.049    0.007 {range}
```
- 从profile结果可以看出父函数foo自己占用的CPU时间并不多，大部分的CPU时间都被子函数bar给占用了。


### 代码下载
本文内容和代码已归档到https://github.com/jumper2014/PyCodeComplete，欢迎star
