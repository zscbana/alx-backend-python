#!/usr/bin/env python3
"""1. Async Comprehensions"""
import asyncio
import random
import typing


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> typing.List[float]:
    """Async comprehension"""
    return [num async for num in async_generator()]
