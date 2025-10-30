"""
Author: chilli, SJTU, pajenegod
Date: 2020-03-04
License: CC0
Source: own
Description: Pollard-rho randomized factorization algorithm. Returns prime
factors of a number, in arbitrary order (e.g. 2299 -> {11, 19, 11}).
Time: O(n^{1/4}), less for numbers with small factors.
Status: stress-tested
"""

import math
from typing import List
from .mod_mul_ll import modmul
from .miller_rabin import is_prime

def pollard(n: int) -> int:
    """Pollard's rho algorithm to find a factor of n"""
    x = 0
    y = 0
    t = 30
    prd = 2
    i = 1
    
    def f(x_val):
        return modmul(x_val, x_val, n) + i
    
    while t % 40 != 0 or math.gcd(prd, n) == 1:
        t += 1
        if x == y:
            i += 1
            x = i
            y = f(x)
        q = modmul(prd, max(x, y) - min(x, y), n)
        if q:
            prd = q
        x = f(x)
        y = f(f(y))
    
    return math.gcd(prd, n)

def factor(n: int) -> List[int]:
    """Factor n into prime factors"""
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    x = pollard(n)
    l = factor(x)
    r = factor(n // x)
    l.extend(r)
    return l

