#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import asyncio


async def work(t, x):
    print('Task {} start'.format(t))
    await  asyncio.sleep(x)
    print('Task {} done'.format(t))
    return "{0}:{1}".format(t, x)

tasks = [
    asyncio.ensure_future(work('a', 2)),
    asyncio.ensure_future(work('b', 3)),
    asyncio.ensure_future(work('c', 1))
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
# 获得协程的执行结果
for task in tasks:
    print('Task return: {}'.format(task.result()))
loop.close()
"""
Task a start
Task b start
Task c start
Task c done
Task a done
Task b done
Task return: a:2
Task return: b:3
Task return: c:1
"""