#!/usr/bin/env python3
'''Task 8's module.'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies its argument by the multiplier.'''
    return lambda x: x * multiplier
