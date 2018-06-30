### print
- python2中print是关键字， python3中print是函数
- python3的print函数原型如下
```
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

### 例子
- sep参数会将前面需要打印的元素用其分割
- end参数指定后，可以避免使用默认的换行符导致的换行
- 其他两个参数很简单，就不讲了
```
if __name__ == '__main__':
    # 把平方计算结果打印在同一行
    for i in range(10):
        print("{0}*{0}".format(i), i*i, sep="=", end="\t")
    
    # 输出如下
    # 0*0=0	1*1=1	2*2=4	3*3=9	4*4=16	5*5=25	6*6=36	7*7=49	8*8=64	9*9=81
```