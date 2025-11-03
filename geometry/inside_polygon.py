"""
Author: Victor Lecomte, chilli
Date: 2019-04-26
License: CC0
Source: https://vlecomte.github.io/cp-geo.pdf
Description: Returns true if p lies within the polygon. If strict is true,
it returns false for points on the boundary. The algorithm uses
products in intermediate steps so watch out for overflow.
Time: O(n)
Status: stress-tested and tested on kattis:pointinpolygon
"""

from typing import List
from .point import Point
from .on_segment import on_segment

def inside_polygon(p: List[Point], a: Point, strict: bool = True) -> bool:
    """
    Check if point a is inside polygon p.
    strict=True: excludes boundary points
    strict=False: includes boundary points
    """
    cnt = 0
    n = len(p)
    
    for i in range(n):
        q = p[(i + 1) % n]
        if on_segment(p[i], q, a):
            return not strict
        cnt ^= ((a.y < p[i].y) - (a.y < q.y)) * a.cross(p[i], q) > 0
    
    return bool(cnt)

