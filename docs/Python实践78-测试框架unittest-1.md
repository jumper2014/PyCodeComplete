### unittest简介
- unittest最初是为了做单元测试而生的，但是现在不仅仅可以做单元测试，其实是一个通用测试框架
- 灵感来自于JUnit等其他主流单元测试框架


### 四大组件
- test fixture: 用来在多个用例之间分享的预置条件操作和清理操作，说白了就是setup和teardown的集合。
- test case: 测试用例，用来放置测试步骤和检查点
- test suite: 测试套件，一组测试用例的集合，用来管理和组织测试用例。
- test runner: 用来执行用例，并且向用户提供测试结果。unittest中的test runner有好几种形式。


### 实力讲解
- 下面这个例子来自官网
```
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
```

- 首先需要引入unittest库
- 测试类必须继承自unittest.TestCase
- 测试用例必须以小写test开头
- 断言函数需要通过测试类的self调用
- 通过调用unittest.main()来执行模块里所有的测试用例
- 执行命令为python unittest_sample1.py
- 执行结果如下：
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

