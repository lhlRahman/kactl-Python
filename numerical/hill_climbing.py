"""
Author: Simon Lindholm
Date: 2015-02-04
License: CC0
Source: Johan Sannemo
Description: Poor man's optimization for unimodal functions.
Status: used with great success
"""

from typing import Tuple, Callable, List

def hill_climb(start: List[float], f: Callable[[List[float]], float]) -> Tuple[float, List[float]]:
    """
    Hill climbing optimization for unimodal functions.
    start = starting point [x, y]
    f = function to minimize
    Returns (min_value, [x, y])
    """
    cur_val = f(start)
    cur_point = start[:]
    
    jmp = 1e9
    while jmp > 1e-20:
        for _ in range(100):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    p = [cur_point[0] + dx * jmp, cur_point[1] + dy * jmp]
                    val = f(p)
                    if val < cur_val:
                        cur_val = val
                        cur_point = p
        jmp /= 2
    
    return (cur_val, cur_point)

