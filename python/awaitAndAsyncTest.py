#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

#This script requires python 3.5+

import asyncio

async def compute():
    for i in range(5):
        print(f"compute {i}")
        await asyncio.sleep(.1)

async def compute2():
    for i in range(5):
        print(f"compute2 {i}")
        await asyncio.sleep(.2)

async def main():
    await asyncio.gather(compute(), compute2())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
