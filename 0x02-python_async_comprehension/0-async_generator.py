#!/usr/bin/env python3
"""function to generate async generator"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """function that will Loop 10 times, wait 1 sec each time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
