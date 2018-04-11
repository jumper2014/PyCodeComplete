### 背景
- 上一篇提到了如何开发一个链家网小区房价的爬虫，其实该爬虫当时是基于Python2.7开发的。
- 如果让你的代码能够同时支持Python2和Python3的话，会有更多的人可以使用。


### 解决方法
- 减少Python2和Python3实现的差异。比如，之前为了减少第三方依赖，我将requests用urllib2来代替，但是Python3中urllib2不好使了，这个时候一种解决方案是，用同时支持Python2和Python3的库来替代urllib2。最后，我还是将requests给替代了回来，唉！
- 还有的包到Python3中改了名字，我们可以在import的时候对这些问题进行处理。
```
try:    #python2
    from UserDict import UserDict
    #建议按照python3的名字进行import
    from UserDict import DictMixin as MutableMapping
except ImportError: #python3
    from collections import UserDict
    from collections import MutableMapping
```
- 如果Python2和Python3之间的代码有较大差异，简单起见，使用sys.version或者sys.version_info来判断Python版本，然后不同的版本使用不同的代码。虽然有点丑陋，但是能够解决问题。
```
if sys.version_info < (3, 0):   # 如果小于Python3
    city = raw_input(prompt)
else:
    city = input(prompt)
```
