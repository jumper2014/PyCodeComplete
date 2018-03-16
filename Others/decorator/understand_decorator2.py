# coding=utf-8
# 可以使用 python的装饰器语法糖@


def connect_db():
    print 'connect db'


def close_db():
    print 'close db'


def query_user():
    print 'query some user'


def query_data(query):
    """ 定义装饰器，返回一个函数，对query进行wrapper包装 """
    def wrapper():
        connect_db()
        query()
        close_db()
    return wrapper


# 使用 @ 调用装饰器进行装饰
@query_data
def query_user():
    print 'query some user'

query_user()
