"""
Author: Bjorn Martinsson
Date: 2020-06-03
License: CC0
Source: own work
Description: Returns the smallest x > 0 s.t. a^x = b (mod m), or
-1 if no such x exists. mod_log(a,1,m) can be used to
calculate the order of a.
Time: O(√m)
Status: tested for all 0 <= a,x < 500 and 0 < m < 500.
"""

import math
from typing import Dict

def mod_log(a: int, b: int, m: int) -> int:
    """
    Discrete logarithm: find smallest x > 0 such that a^x ≡ b (mod m)
    Returns -1 if no solution exists
    Uses baby-step giant-step algorithm
    """
    n = int(math.sqrt(m)) + 1
    e = 1
    f = 1
    j = 1
    A: Dict[int, int] = {}
    
    # Baby step
    while j <= n:
        e = f = e * a % m
        if e == b % m:
            return j
        A[e * b % m] = j
        j += 1
    
    # Giant step
    if math.gcd(m, e) == math.gcd(m, b):
        for i in range(2, n + 2):
            e = e * f % m
            if e in A:
                return n * i - A[e]
    
    return -1

