### pairwise算法
- Pairwise是L. L. Thurstone(29 May1887 – 30 September 1955)在1927年首先提出来的。他是美国的一位心理统计学家。Pairwise也正是基于数学统计和对传统的正交分析法进行优化后得到的产物。
- Pairwise基于如下2个假设：
（1）每一个维度都是正交的，即每一个维度互相都没有交集。
（2）根据数学统计分析，73%的缺陷（单因子是35%，双因子是38%）是由单因子或2个因子相互作用产生的。19%的缺陷是由3个因子相互作用产生的。
- 因此，pairwise基于覆盖所有2因子的交互作用产生的用例集合性价比最高而产生。

### 使用AllPairs构建pairwise测试用例集
- AllPairs模块官网https://pypi.python.org/pypi/AllPairs/2.0.1
- 安装：pip install allpairs

### 实例
- 假设我们要构建一组弱网条件下的测试用例的集合，影响因素有：网络带宽，丢包了，网络延迟
- 每个因素都有多个需要测试的条件，比如网络带宽分别需要测试1M,3M,5M,10M
- 下面的代码演示了如何使用allpairs来生成两两的正交测试条件
```
import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

if __name__ == '__main__':
    # 带宽，丢包，延迟
    parameters = [
        ["1M", "3M", "5M", "10M"],
        ["1%", "5%", "10%", "15%"],
        ["0ms", "50ms", "100ms", "200ms"]
    ]

    pairwise = all_pairs(parameters)
    for i, v in enumerate(pairwise):
        print("%i:\t%s" %(i, str(v)))

    """
    0:	['1M', '1%', '0ms']
    1:	['3M', '5%', '0ms']
    2:	['5M', '10%', '0ms']
    3:	['10M', '15%', '0ms']
    4:	['10M', '10%', '50ms']
    5:	['5M', '5%', '50ms']
    6:	['3M', '1%', '50ms']
    7:	['1M', '15%', '50ms']
    8:	['1M', '10%', '100ms']
    9:	['3M', '15%', '100ms']
    10:	['5M', '1%', '100ms']
    11:	['10M', '5%', '100ms']
    12:	['10M', '1%', '200ms']
    13:	['5M', '15%', '200ms']
    14:	['3M', '10%', '200ms']
    15:	['1M', '5%', '200ms']
    """
```