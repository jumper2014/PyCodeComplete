### Python里面没有switch-case
- Python社区认为使用if-elif-else结构完全能够做到和switch-case一样的事情
- 曾经有一些关于switch-case表达式的提案，因为支持的人不多，所以没有能被采纳

### 如何实现类似功能
- 使用if-elif-else结构，适用于选择分支不多的情况，例如：
```
if __name__ == '__main__':
    option = raw_input("input:")
    if option == "start":
        print("start app")
    elif option == "stop":
        print("stop app")
    elif option == "restart":
        print("restart app")
```

- 使用字典+函数，适用于选择分支多的情况。字典的key是条件，值是满足条件时执行的目标函数，例如：
```
def start_app():
    print("start app")
    
def stop_app():
    print("stop app")

def restart_app():
    print("restart app")

switch = {
    "start": start_app,
    "stop": stop_app,
    "restart": restart_app
}

if __name__ == '__main__':
    option = raw_input("input:")
    switch[option]()
```

### 代码下载
本文地址已经归档到https://github.com/jumper2014/PyCodeComplete，欢迎star