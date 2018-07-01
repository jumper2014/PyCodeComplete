### timeit模块
- timeit模块可以用来多次重复运行某段代码，度量其运行用时
- 你可以在Python脚本中使用timeit模块，也可以通过命令行使用timeit模块

### 主要函数
- timeit(stmt='pass', setup='pass', timer=<defaulttimer>, number=1000000)

       返回：

            返回执行stmt这段代码number遍所用的时间，单位为秒，float型

       参数：

            stmt：要执行的那段代码

            setup：执行代码的准备工作，不计入时间，一般是import之类的

            timer：这个在win32下是time.clock()，linux下是time.time()，默认的，不用管

            number：要执行stmt多少遍

- repeat(stmt='pass', setup='pass', timer=<defaulttimer>, repeat=3, number=1000000)

       这个函数比timeit函数多了一个repeat参数而已，表示重复执行timeit这个过程多少遍，返回一个列表，表示执行每遍的时间

### 例子
```
import random
import timeit


def random_sort():
    return sorted([random.random() for i in range(2000000)])


if __name__ == "__main__":
    # 相当于命令行下的
    # python -m timeit -n 1 -s "import random; sorted([random.random() for i in range(2000000)])"
    t1 = timeit.timeit(stmt=random_sort, number=1)
    print(t1)

    # 相当于命令行下的
    # python -m timeit -n 2 -r 2 -s "import random; sorted([random.random() for i in range(2000000)])"
    t2 = timeit.repeat(stmt=random_sort, number=2, repeat=2)
    print(t2)
```

### 注意
- timeit模块暂时禁用了垃圾收集器，如果你的操作会调用到垃圾收集器，那么它有可能会影响到你的实际操作速度。
- 当从命令行运行timeit时，timeit会对语句执行n次并计算平均值作为一个结果，重复r次并选出最好的哪个结果。


### 代码下载
本文内容和代码已归档到https://github.com/jumper2014/PyCodeComplete，欢迎star