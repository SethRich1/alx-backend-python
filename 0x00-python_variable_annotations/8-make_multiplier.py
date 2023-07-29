#!/usr/bin/env python3
""" a python script to annotate a callable"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function to return a callable annotation"""
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
