#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import asyncio


async def main():
    print('hello')
    await  asyncio.sleep(1)
    print('world')

loop = asyncio.get_event_loop()
task = loop.create_task(main())
print(task)  # pending状态的Task
loop.run_until_complete(task)
print(task)     # finished状态的Task
print(isinstance(task, asyncio.Future))  # True
loop.close()