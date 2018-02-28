#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import asyncio
import time
import aiohttp

now = lambda: time.time()

async def do_some_work(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # print(resp.status)
            return await resp.text()

async def main():
    urls = ['http://api.bilibili.com/x/web-interface/archive/stat?aid={0}'.format(x) for x in range(1, 1001)]
    tasks = [asyncio.ensure_future(do_some_work(url)) for url in urls]
    done, pending = await asyncio.wait(tasks)
    for task in done:
        print('Task ret: ', task.result())
    # for task in pending:
    #     print(task)

start = now()

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main())

try:
    loop.run_until_complete(task)
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

print('TIME: ', now() - start)