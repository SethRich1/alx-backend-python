#!/usr/bin/env python3
""" a python script to find sum of a int and float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function to return sum of a float and int"""
    return sum(mxd_lst)
