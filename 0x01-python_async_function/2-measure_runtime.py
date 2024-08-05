#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio


wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) 