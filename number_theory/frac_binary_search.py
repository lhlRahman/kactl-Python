"""
Author: Lucian Bicsi, Simon Lindholm
Date: 2017-10-31
License: CC0
Description: Given f and N, finds the smallest fraction p/q in [0, 1]
such that f(p/q) is true, and p, q <= N.
Time: O(log(N))
Status: stress-tested for n <= 300
"""

from typing import Callable, Tuple

class Frac:
    def __init__(self, p: int, q: int):
        self.p = p
        self.q = q

def frac_binary_search(f: Callable[[Frac], bool], N: int) -> Tuple[int, int]:
    """
    Binary search over fractions.
    f = predicate function taking a Frac
    N = maximum value for p and q
    Returns (p, q) where p/q is the smallest fraction satisfying f
    """
    dir_flag = True
    A = True
    B = True
    lo = Frac(0, 1)
    hi = Frac(1, 1)  # Set to Frac(1, 0) to search (0, N]
    
    if f(lo):
        return (lo.p, lo.q)
    
    assert f(hi), "f(1/1) must be true"
    
    while A or B:
        adv = 0
        step = 1
        
        # Binary search for advancement
        si = 0
        while step:
            adv += step
            mid = Frac(lo.p * adv + hi.p, lo.q * adv + hi.q)
            
            if abs(mid.p) > N or mid.q > N or dir_flag == (not f(mid)):
                adv -= step
                si = 2
            
            if si == 2:
                si = 0
            step = (step * 2) >> si if step else 0
        
        hi.p += lo.p * adv
        hi.q += lo.q * adv
        dir_flag = not dir_flag
        lo, hi = hi, lo
        A = B
        B = bool(adv)
    
    return (hi.p, hi.q) if dir_flag else (lo.p, lo.q)

