### cProfile生成二进制结果文件
- cProfile模块提供一个功能，可以将profile结果保存为二进制文件
- 通过cProfile命令行生成二进制结果文件: python -m cProfile -o result.out foobar.py
- 通过cProfile代码生成二进制结果文件: cProfile.run("foo()", filename="result.out")
- 
### pstats模块
- Python提供了一个pstats模块，用来分析cProfile输出的文件内容。
- 需要导入pstats模块, import pstats
- 通过加载result.out来创建Stats对象，然后调用Stats对象的方法来打印profile结果

### 举个栗子
- 首先使用上一篇的代码，生成result.out文件
- 使用pstats模块的代码如下
```
    # 创建Stats对象
    p = pstats.Stats("result.out")

    # strip_dirs(): 去掉无关的路径信息
    # sort_stats(): 排序，支持的方式和上述的一致
    # print_stats(): 打印分析结果，可以指定打印前几行

    # 按照函数名排序，只打印前3行函数的信息, 参数还可为小数,表示前百分之几的函数信息
    p.strip_dirs().sort_stats("name").print_stats(3)

    # 按照运行时间和函数名进行排序
    p.strip_dirs().sort_stats("cumulative", "name").print_stats(0.8)

    # 如果想知道有哪些函数调用了bar
    p.print_callers("bar")

    # 查看test()函数中调用了哪些函数
    p.print_callees("foo")
```
- 输出结果如下
```
Sun Mar 25 16:37:01 2018    result.out

         15 function calls in 0.227 seconds

   Ordered by: function name
   List reduced from 5 to 3 due to restriction <3>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.227    0.227 <string>:1(<module>)
        7    0.039    0.006    0.039    0.006 {range}


Sun Mar 25 16:37:01 2018    result.out

         15 function calls in 0.227 seconds

   Ordered by: cumulative time, function name
   List reduced from 5 to 4 due to restriction <0.8>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.227    0.227 <string>:1(<module>)
        1    0.004    0.004    0.227    0.227 foobar.py:13(foo)
        5    0.184    0.037    0.223    0.045 foobar.py:6(bar)
        7    0.039    0.006    0.039    0.006 {range}


   Ordered by: cumulative time, function name
   List reduced from 5 to 2 due to restriction <'bar'>

Function           was called by...
                       ncalls  tottime  cumtime
foobar.py:13(foo)  <-       1    0.004    0.227  <string>:1(<module>)
foobar.py:6(bar)   <-       5    0.184    0.223  foobar.py:13(foo)


   Ordered by: cumulative time, function name
   List reduced from 5 to 2 due to restriction <'foo'>

Function           called...
                       ncalls  tottime  cumtime
foobar.py:13(foo)  ->       5    0.184    0.223  foobar.py:6(bar)
                            2    0.001    0.001  {range}
foobar.py:6(bar)   ->       5    0.038    0.038  {range}
```
- 结果列的含义如下
```
    ncalls：表示函数调用的次数；
    tottime：表示指定函数的总的运行时间，除掉函数中调用子函数的运行时间；
    percall：（第一个percall）等于 tottime/ncalls；
    cumtime：表示该函数及其所有子函数的调用运行的时间，即函数开始调用到返回的时间；
    percall：（第二个percall）即函数运行一次的平均时间，等于 cumtime/ncalls；
    filename:lineno(function)：每个函数调用的具体信息；
```

