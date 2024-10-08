#!/usr/bin/env python3
""" synchronous coroutine that takes in an integer argument """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine that takes in an integer argument """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
