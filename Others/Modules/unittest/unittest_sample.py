# coding=utf-8

import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print 'Case Before'

    def tearDown(self):
        print 'Case After'

    def test_upper(self):
        print("TC test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("TC test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("TC test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

if __name__ == '__main__':
    # unittest.main()

    # 创建测试集合,并且添加测试用例到测试集合
    suiteTest = unittest.TestSuite()

    suiteTest.addTest(TestStringMethods('test_upper'))
    suiteTest.addTest(TestStringMethods('test_split'))

    # 通过test runner启动测试集合
    runner = unittest.TextTestRunner()
    runner.run(suiteTest)