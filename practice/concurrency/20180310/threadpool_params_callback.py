#!/usr/bin/env python
# coding=utf-8
# 演示threadpool多参数和处理结果

import threadpool
import time


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


