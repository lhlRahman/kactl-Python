"""
Author: Simon Lindholm
Date: 2015-05-12
License: CC0
Source: own work
Description:
Find the smallest i in [a,b] that maximizes f(i), assuming that f(a) < ... < f(i) >= ... >= f(b).
To minimize f, change < to >.
Time: O(log(b-a))
Status: tested
"""

from typing import Callable

def ternary_search(a: int, b: int, f: Callable[[int], float]) -> int:
    """
    Find the index that maximizes f in range [a, b].
    Assumes f is unimodal (increases then decreases).
    """
    assert a <= b
    while b - a >= 5:
        mid = (a + b) // 2
        if f(mid) < f(mid + 1):
            a = mid
        else:
            b = mid + 1
    
    # Linear search in remaining range
    best = a
    for i in range(a + 1, b + 1):
        if f(best) < f(i):
            best = i
    
    return best
