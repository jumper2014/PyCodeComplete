### 背景
- 前面一篇介绍了使用命令行来profile你的Python程序，本篇介绍在代码里面调用cProfile模块来分析
- 需要先import cProfile
- 然后调用run函数来profile指定的函数

### 例子
- 还是上篇的代码，父函数foo()调用子函数bar()
```
def bar():
    result = 0
    for i in range(1000000):
        result += i
    return result


def foo():
    result = 0
    for i in range(100000):
        result += i
    for i in range(5):
        bar()
    return result


if __name__ == '__main__':
    import cProfile

    # 直接把分析结果打印到控制台
    cProfile.run("foo()")

    # 根据cumtime列排序后打印到控制台，
    # 也就是说按包含子函数执行的时间顺序进行排序
    cProfile.run("foo()", sort="cumulative")
```
- 下面是执行结果：
```
Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.278    0.278 <string>:1(<module>)
        1    0.005    0.005    0.278    0.278 foobar.py:13(foo)
        5    0.207    0.041    0.270    0.054 foobar.py:6(bar)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        7    0.066    0.009    0.066    0.009 {range}


         15 function calls in 0.229 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.229    0.229 <string>:1(<module>)
        1    0.004    0.004    0.229    0.229 foobar.py:13(foo)
        5    0.188    0.038    0.225    0.045 foobar.py:6(bar)
        7    0.037    0.005    0.037    0.005 {range}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

