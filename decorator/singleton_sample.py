# coding=utf-8
# 单例模式


def singleton(cls):
    instances = dict()

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class MyClass(object):
    pass


if __name__ == "__main__":
    t1 = MyClass()
    t2 = MyClass()
    print id(t1)
    print id(t2)
