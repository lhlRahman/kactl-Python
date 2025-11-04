"""
Author: Simon Lindholm
Date: 2015-03-20
License: CC0
Source: me
Description: Split a monotone function on [from, to) into a minimal set of half-open intervals on which it has the same value.
Runs a callback g for each such interval.
Time: O(k * log(n/k))
Status: tested
"""

from typing import Callable, Any

def constant_intervals(from_val: int, to_val: int, 
                      f: Callable[[int], Any], 
                      g: Callable[[int, int, Any], None]):
    """
    Split monotone function into constant intervals.
    from_val, to_val = range [from_val, to_val)
    f = monotone function
    g = callback(lo, hi, val) for each constant interval [lo, hi)
    """
    if to_val <= from_val:
        return
    
    i = from_val
    p = f(i)
    q = f(to_val - 1)
    
    def rec(from_idx, to_idx, i_ref, p_ref, q_val):
        """Recursive helper"""
        if p_ref == q_val:
            return i_ref, p_ref
        
        if from_idx == to_idx:
            g(i_ref, to_idx, p_ref)
            return to_idx, q_val
        else:
            mid = (from_idx + to_idx) >> 1
            i_ref, p_ref = rec(from_idx, mid, i_ref, p_ref, f(mid))
            i_ref, p_ref = rec(mid + 1, to_idx, i_ref, p_ref, q_val)
            return i_ref, p_ref
    
    i, p = rec(from_val, to_val - 1, i, p, q)
    g(i, to_val, q)

