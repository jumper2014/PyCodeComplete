#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import aiohttp
import asyncio


async def main(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            print(await resp.text())

url = 'https://zhuanlan.zhihu.com/python2018'
loop = asyncio.get_event_loop()
loop.run_until_complete(main(url))