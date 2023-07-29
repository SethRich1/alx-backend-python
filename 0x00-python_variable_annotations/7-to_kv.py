#!/usr/bin/env python3
""" a python script to return a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function to return a tuple annotation"""
    return (k, (v ** 2))
