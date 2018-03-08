### 一般形式
- reduce()函数接受两个参数，形如reduce(func, seq)
- 第一个参数func是一个二元函数(接收两个值作为输入)
- 第二个参数seq是一个序列
- reduce()将第一次从seq序列中取前两个元素，喂给函数func调用，得到一个中间结果，然后将该结果和seq里的下一个元素再喂给func，依此反复，直到seq中所有的元素被遍历完
- 最终结果被reduce()返回


### 例子
- reduce()特别适合进行累计求值
- 下面的例子演示如何使用reduce()进行求和和求积
```
# 计算和
sum_result = reduce(lambda x, y: x+y, range(1, 10))
assert(sum_result == 45)
print(sum_result)

# 计算阶乘
factorial_result = reduce(lambda x, y: x * y, range(1, 10))
assert(factorial_result == 362880)
print(factorial_result)
```

### 代码下载
本文地址已经归档到github，您可以访问下面的链接获得。  
[代码地址](https://github.com/jumper2014/Asgard/tree/master/practice/func/20180118)

如果觉得本文对您有帮助，敬请点赞。



