"""
Author: Johan Sannemo
License: CC0
Description: Compute indices of smallest set of intervals covering another interval.
Intervals should be [inclusive, exclusive). 
Returns empty set on failure (or if G is empty).
Time: O(N log N)
Status: Tested on kattis:intervalcover
"""

from typing import List, Tuple, TypeVar

T = TypeVar('T')

def interval_cover(G: Tuple[T, T], I: List[Tuple[T, T]]) -> List[int]:
    """
    Find minimum set of intervals from I that cover interval G.
    G: interval to cover (inclusive, exclusive)
    I: list of available intervals (inclusive, exclusive)
    Returns: indices of intervals that form the cover, or [] if impossible
    """
    S = sorted(range(len(I)), key=lambda i: I[i])
    R = []
    cur = G[0]
    at = 0
    
    while cur < G[1]:
        mx = (cur, -1)
        while at < len(I) and I[S[at]][0] <= cur:
            mx = max(mx, (I[S[at]][1], S[at]))
            at += 1
        
        if mx[1] == -1:
            return []
        cur = mx[0]
        R.append(mx[1])
    
    return R

