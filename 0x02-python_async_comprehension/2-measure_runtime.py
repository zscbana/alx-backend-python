#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import asyncio
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of four parallel comprehensions"""
    Start_time = time.time()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    return time.time() - Start_time
