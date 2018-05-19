### fixture的类型
- Python unittest主要有三种fixture
- setUp, tearDown每个测试类的用例都会执行
- setUpClass, tearDownClass每个类的第一个用例被执行前和最后一个用例执行后被执行
- setUpModule, tearDownModule每个测试模的第一个用例被执行前和最后一个用例执行后被执行

### 出现异常
- 如果setup和teardown间的用例出现异常或者失败，teardown照样会被执行
- 如果setUpClass和setUpModule中出现异常，那么他们控制范围内的用例不会被执行，并且对应的tearDownClass和tearDownModule也不会被执行

### 用一个例子看看执行顺序
```
import unittest


def setUpModule():
    print("setUpModule >>>")


def tearDownModule():
    print("tearDownModule >>>")


class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass for Test1 >>")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass for Test1 >>")

    def setUp(self):
        print("setUp for Test1 >")

    def tearDown(self):
        print("tearDown for Test1 >")

    def testCase1(self):
        print("testCase1 for Test1")

    def testCase2(self):
        print("testCase2 for Test1")


class Test2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass for Test2 >>")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass for Test2 >>")

    def setUp(self):
        print("setUp for Test2 >")

    def tearDown(self):
        print("tearDown for Test2 >")

    def testCase1(self):
        print("testCase1 for Test2")

    def testCase2(self):
        print("testCase2 for Test2")


if __name__ == "__main__":
    unittest.main()
```
- 执行结果如下：
```
setUpModule >>>
setUpClass for Test1 >>
setUp for Test1 >
testCase1 for Test1
tearDown for Test1 >
setUp for Test1 >
testCase2 for Test1
tearDown for Test1 >
tearDownClass for Test1 >>
setUpClass for Test2 >>
setUp for Test2 >
testCase1 for Test2
tearDown for Test2 >
setUp for Test2 >
testCase2 for Test2
tearDown for Test2 >
tearDownClass for Test2 >>
tearDownModule >>>
```