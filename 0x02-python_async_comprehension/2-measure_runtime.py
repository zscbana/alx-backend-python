#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import asyncio
import random
import typing
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension

async def measure_runtime() -> float:
    """Measure the runtime of four parallel comprehensions"""
    Start_time= time.time()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    end_time = time.time()
    return (Start_time - end_time)
