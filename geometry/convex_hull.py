"""
Author: Stjepan Glavina, chilli
Date: 2019-05-05
License: Unlicense
Source: https://github.com/stjepang/snippets/blob/master/convex_hull.cpp
Description: Returns a vector of the points of the convex hull in counter-clockwise order.
Points on the edge of the hull between two other points are not considered part of the hull.
Time: O(n log n)
Status: stress-tested, tested with kattis:convexhull
"""

from typing import List
from .point import Point

def convex_hull(pts: List[Point]) -> List[Point]:
    """Compute convex hull of points"""
    if len(pts) <= 1:
        return pts
    
    pts = sorted(pts)
    h = [None] * (len(pts) + 1)
    s = 0
    t = 0
    
    for it in range(2):
        for p in pts:
            while t >= s + 2 and h[t - 2].cross(h[t - 1], p) <= 0:
                t -= 1
            h[t] = p
            t += 1
        s = t - 1
        t -= 1
        pts.reverse()
    
    # Remove duplicate if hull has only 2 points and they're the same
    end = t - (1 if t == 2 and h[0] == h[1] else 0)
    return h[:end]

