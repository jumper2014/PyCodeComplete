# coding=utf-8


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

# 这里调用query_data进行实际装饰（注意装饰是动词）
query_user = query_data(query_user)

# 调用被装饰后的函数query_user
query_user()
