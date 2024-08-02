#!/usr/bin/env python3
'''Task 11's module.'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Returns the value of the key in the dictionary if it exists,
      otherwise returns the default value'''
    if key in dct:
        return dct[key]
    else:
        return default
