### Python命令行选项
- 打印帮助
> - python -h 
> - python --help

- 打印版本
> - python -V (注意大写V)
> - python --version

- 优化
> - python -O 打开基本优化。这将编译（字节码）文件的文件扩展名从.pyc更改为.pyo

- 打开hash随机化
> - python -R

- 强制stdion, stdout和stderr完全无缓冲
> - python -u

- 警告控制
> - python -W ignore 忽略所有警告。
> - python -W default 明确请求默认行为（每个源代码行打印每个警告一次）。
> - python -W all 每次发生警告时都会发出警告（如果对同一源代码行重复触发警告（例如循环内），则可能会生成许多消息）。
> - python -W module 仅在每个模块中第一次出现时才打印每个警告。
> - python -W once 仅在程序中第一次出现时才打印每个警告。
> - python -W error 引发异常而不是打印警告消息。

- 在命令行中执行Python代码
> - python -c <command> 在命令中执行Python代码。 命令可以是一个或多个由换行符分隔的语句，与正常模块代码一样具有显着的前导空白。如果给出了这个选项，第一个元素sys.argv将是 "-c"，并且当前目录将被添加到开始处 sys.path（允许将该目录中的模块作为顶级模块导入）。
> 
> 
> - python -c "import time; print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))" 利用python打印当前时间

- 将模块当做script运行
> - python -m <module-name>
> 搜索sys.path指定的模块并将其内容作为__main__模块执行。由于参数是模块名称，因此您不得提供文件扩展名（.py）。本module-name应该是一个有效的Python模块名称，但执行并不总是执行这项（例如，它可以让你使用包含一个连字符的名称）。包名称也是允许的。当提供包名称而不是普通模块时，解释器将<pkg>.__main__作为主模块执行。 如果给出该选项，则第一个元素sys.argv将是模块文件的完整路径。与-c选项一样，当前目录将被添加到开始sys.path。
> - python -m timeit
> - python -m SimpleHTTPServer