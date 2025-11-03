"""
Author: Oleksandr Bacherikov, chilli
Date: 2019-05-07
License: Boost Software License
Source: https://github.com/AlCash07/ACTL
Description: Line-convex polygon intersection. The polygon must be ccw and have no collinear points.
line_hull returns a pair describing the intersection:
  (-1, -1) if no collision
  (i, -1) if touching corner i
  (i, i) if along side (i, i+1)
  (i, j) if crossing sides (i, i+1) and (j, j+1)
Time: O(log n)
Status: stress-tested
"""

from typing import List, Tuple
from .point import Point
from .side_of import sgn

def extr_vertex(poly: List[Point], dir: Point) -> int:
    """Find extreme vertex in direction dir"""
    n = len(poly)
    
    def cmp(i, j):
        return sgn(dir.perp().cross(poly[i % n] - poly[j % n]))
    
    def extr(i):
        return cmp(i + 1, i) >= 0 and cmp(i, i - 1 + n) < 0
    
    if extr(0):
        return 0
    
    lo = 0
    hi = n
    while lo + 1 < hi:
        m = (lo + hi) // 2
        if extr(m):
            return m
        ls = cmp(lo + 1, lo)
        ms = cmp(m + 1, m)
        if ls < ms or (ls == ms and ls == cmp(lo, m)):
            hi = m
        else:
            lo = m
    
    return lo

def line_hull(a: Point, b: Point, poly: List[Point]) -> Tuple[int, int]:
    """
    Find intersection of line through a,b with convex polygon.
    Returns (i, j) as described in docstring.
    """
    n = len(poly)
    
    def cmpL(i):
        return sgn(a.cross(poly[i], b))
    
    endA = extr_vertex(poly, (a - b).perp())
    endB = extr_vertex(poly, (b - a).perp())
    
    if cmpL(endA) < 0 or cmpL(endB) > 0:
        return (-1, -1)
    
    res = [0, 0]
    for i in range(2):
        lo = endB
        hi = endA
        while (lo + 1) % n != hi:
            m = ((lo + hi + (0 if lo < hi else n)) // 2) % n
            if cmpL(m) == cmpL(endB):
                lo = m
            else:
                hi = m
        res[i] = (lo + (1 if not cmpL(hi) else 0)) % n
        endA, endB = endB, endA
    
    if res[0] == res[1]:
        return (res[0], -1)
    
    if not cmpL(res[0]) and not cmpL(res[1]):
        diff = (res[0] - res[1] + n + 1) % n
        if diff == 0:
            return (res[0], res[0])
        if diff == 2:
            return (res[1], res[1])
    
    return tuple(res)

