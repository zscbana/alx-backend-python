#!/usr/bin/env python3
'''Task 9's module.'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of tuples where each tuple contains a sequence from the input'''
    return [(i, len(i)) for i in lst]
