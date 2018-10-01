### 为啥还要聊废弃的库
- 已有代码拿过来直接改改就可以用
- 写前一讲时还没有完全吃透，所以想继续深入了解下
- 网上相关的内容很少，很多也没有说清楚

### 传多参数给任务函数
- makeRequests的原型如下 def makeRequests(callable_, args_list, callback=None,
        exc_callback=_handle_thread_exception)，可以看出第一个参数是线程将要启动任务函数，第二个是要传个任务函数的参数列表，第三个是回调函数，可以用于收集任务结束后的结果或者环境清理
- ``args_list`` 中每一项要么是一个单独的变量，要么是一个2个元素的元组，该元组第1项是位置参数的列表，该元组的第2项是关键参数的字典（很绕口，但最重要）
- 任务函数的多参数，你可以统统通过位置参数列表传进去，也可以统统通过关键字参数字典传进去，也可以通过混合方式传进去
- 例如你的任务函数有两个参数，一个是name，一个是age，那么你可以传args_list为[(['python', 12], None), ]这样的形式， None是未传递的关键字参数字典。
- 也可以传args_list为[(None, {'name':'python', 'age': 12}), ]这样的形式，None是未传递的位置参数列表。
- 还可以传args_list为[(['python'], {'age': 12}), ]这样的形式，这就是混合形式
- 个人感觉太灵活了，而且不好理解

### 结果收集用callback参数
- callback必须接受2个匿名参数， 按顺序分别是WorkRequest对象和任务函数的结果。


### 举个栗子
```
def save_callback(request, result):
    # 第1个参数是request，可以访问request.requestID
    # 第2个参数是request执行完的结果
    print(request.requestID, result)
    with open('result.txt', 'a') as f:
        f.write(result + '\n')


def get_user_info(uid, sex, name, age):
    time.sleep(0.3)
    return "{0},{1},{2},{3}".format(uid, sex, name, age)


if __name__ == '__main__':
    num = 100
    para_list = [[i, 'male'] for i in range(1, num)]
    users = list()
    for i in range(1, num):
        user = {'name'.format(i): 'user{0}'.format(i),
                'age': i}
        users.append(user)
    params = zip(para_list, users)
    # print(params)
    # 形如[([1, 'male'], {'age': 1, 'name': 'user1'}), ...]的参数列表

    pool_size = 10
    pool = threadpool.ThreadPool(pool_size)
    requests = threadpool.makeRequests(get_user_info, params, save_callback)
    [pool.putRequest(req) for req in requests]
    pool.wait()
```

### 代码下载
本文内容和代码已经归档到https://github.com/jumper2014/PyCodeComplete，欢迎star