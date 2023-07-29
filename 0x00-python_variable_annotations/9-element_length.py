#!/usr/bin/env python3
""" a python script to annonate a sequence"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function to return a sequence"""
    return [(i, len(i)) for i in lst]
