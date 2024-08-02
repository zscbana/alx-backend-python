#!/usr/bin/env python3
'''Task 7's module.'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple. The first element of the tuple is the string k.
    The second element is the square of the int/float
    v and should be annotated as a float."""
    return k, float(v ** 2)
