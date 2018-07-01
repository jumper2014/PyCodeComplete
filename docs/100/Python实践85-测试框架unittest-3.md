### 运行指定的用例
- 使用unittest.main()会运行该模块中的所有用例
- 想要运行指定的用例需要将这些用例加入测试套件TestSuite中来运行，主要是4步
- 1. 新建一个测试套件TestSuite
- 2. 将测试用例一个一个加入该TestSuite
- 3. 新建一个TestRunner
- 4. 用该TestRunner来运行TestSuite

### 一个例子
```
import unittest


class Count(object):
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b


class TestCount(unittest.TestCase):
    def setUp(self):
        print("Test Start")

    def tearDown(self):
        print("Test End")

    def test_add1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(3, 3)
        self.assertEqual(j.add(), 5)


if __name__ == "__main__":
    # 1. 新建测试套件
    suite = unittest.TestSuite()
    # 2. 将用例加入测试套件
    suite.addTest(TestCount("test_add1"))
    suite.addTest(TestCount("test_add2"))
    # 3. 新建TestRunner
    runner = unittest.TextTestRunner()
    # 4. 用TestRunner来执行TestSuite
    runner.run(suite)
```