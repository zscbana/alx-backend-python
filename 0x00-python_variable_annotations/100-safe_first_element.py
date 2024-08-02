#!/usr/bin/env python3
'''Task 10's module.'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns the first element of a list if it exists, otherwise None.'''
    if lst:
        return lst[0]
    else:
        return None
