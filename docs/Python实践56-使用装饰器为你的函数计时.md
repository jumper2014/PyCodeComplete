### 背景
- 性能调优需要通过某种方法发现程序的瓶颈
- 性能调优需要准确获得调优前后的性能数据，作为判断调优是否成功的依据
- 装饰器是一种简单而又直接的对函数计时的方法

### 步骤
- 写一个装饰器函数，在被装饰的函数调用前后分别计时，打印计时结果
- 使用该装饰器来装饰被计时的函数

### 例子
```
import time
from functools import wraps
import random


def fn_timer(func):
    @wraps(func)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
               (func.func_name, str(t1 - t0))
               )
        return result

    return function_timer


@fn_timer
def random_sort(n):
    return sorted([random.random() for i in range(n)])


if __name__ == "__main__":
    random_sort(2000000)
    # Total time running random_sort: 1.60562682152 seconds
```

### 代码下载
本文内容和代码已归档到https://github.com/jumper2014/PyCodeComplete，欢迎star