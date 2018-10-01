### StringIO简介
- Python内置的io包里面有一个StringIO类，可以在内存中读写字符串
- 当在StringIO对象上调用close后，文本缓冲区将被清空。
- 可以通过初始化函数来初始化一段内存，也可以通过write函数将字符串写入内存。
- getvalue()函数用来返回内存缓冲区的所有内容。
- 内存缓冲区的内容也可以通过readline()这样的函数读取。

### 举个例子
```
import io

if __name__ == '__main__':

    output = io.StringIO()
    output.write('First line.\n')
    print('Second line.', file=output)

    # 获得对象内容
    contents = output.getvalue()
    print(contents)
    """
    First line.
    Second line.
    """

    # 关闭对象，并且丢弃内存缓存
    # 如果此后再调用getvalue()将会抛出异常
    output.close()

    # 通过初始化函数创建对象
    f = io.StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = f.readline()
        if s == '':     # 如果到达结尾
            break
        print(s.strip())
    f.close()
    """
    Hello!
    Hi!
    Goodbye!
    """
```