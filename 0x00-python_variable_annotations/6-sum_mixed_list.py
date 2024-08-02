#!/usr/bin/env python3
'''Task 6's module.'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''Calculates the sum of a mixed list of integers and floats.'''
    return sum(mxd_lst)
