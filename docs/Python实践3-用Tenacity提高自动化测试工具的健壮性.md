### 背景
在自动化测试工具和自动化测试用例开发过程中，经常需要处理一些待操作对象不稳定的情况，例如，某些界面元素不能及时出现，某些服务暂时不可用。这个时候，测试代码必须想方设法应对这种情况，以便提高工具和用例的健壮性，最常见的解决方法就是进行重试：当特定条件不满足的时候，等待一段时间，然后再次尝试，直到期望的条件满足继续运行，或者重试到达一定数目抛出异常退出。

下面是一种常用的重试代码样板.
```
def do_something_unreliable(retry=10):
    for i in range(retry):
        try:
            if random.randint(0, 10) > 1:
                raise IOError("Unstable status, try again")
            else:
                print("Get stable result")
                return
        except Exception as e:
            print(e.message)
```

其实，已经有高人开发了一个名叫Tenacity的Python库，帮我们优雅地搞定这些需要重试的情况了，使用起来非常简单。
我们可以用pip install tenacity来安装这个库，然后用@retry装饰器来重构上面的代码。
```
from tenacity import retry

@retry
def do_something_unreliable():
    if random.randint(0, 10) > 1:
        raise IOError("Unstable status, try again")
    else:
        print("Get stable result")
        return
```
上面的例子，实现了遇到异常就重试，如果想要限制重试次数，只需要修改@retry装饰器那一行即可。
```
from tenacity import retry, stop_after_attempt
@retry(stop=stop_after_attempt(3))
```
如果想要每5秒钟重试一次
```
from tenacity import retry, wait_fixed
@retry(wait=wait_fixed(5))
```
上面这些，仅仅是tenacity最简单的使用方法，其他重试的方式还有很多种，大家可以访问http://tenacity.readthedocs.io/en/latest/ 找到更多的使用方法。

当然，看到好东西，就应该把它用起来，今天我已经把常用的多节点存活状态采集的自动化工具用tenacity改进了一版，以前必须要用较长的超时机制(requests的timeout参数）来对抗网络异常，现在只新加两行代码，就大大缩短了统计时间，增强了健壮性，优雅地不得了。

### 代码地址
对了，本文的例子，大家可以访问github获得。欢迎star
https://github.com/jumper2014/PyCodeComplete
