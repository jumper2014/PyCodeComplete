#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import asyncio


async def main():
    print('hello')
    await  asyncio.sleep(1)
    print('world')
    return 'hello world'

loop = asyncio.get_event_loop()
# 定义一个future
task = asyncio.ensure_future(main())
loop.run_until_complete(task)
# 获得协程的执行结果
print('Task return: {}'.format(task.result()))
loop.close()
"""
hello
world
Task return: hello world
"""