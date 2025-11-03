"""
Author: chilli
Date: 2019-05-17
License: CC0
Source: https://github.com/ngthanhtrung23/ACM_Notebook_new
Description: Determine whether a point t lies inside a convex hull (CCW
order, with no collinear points). Returns true if point lies within
the hull. If strict is true, points on the boundary aren't included.
Time: O(log N)
Status: stress-tested
"""

from typing import List
from .point import Point
from .side_of import side_of, sgn
from .on_segment import on_segment

def point_inside_hull(l: List[Point], p: Point, strict: bool = True) -> bool:
    """
    Check if point p is inside convex hull l.
    Hull must be in CCW order with no collinear points.
    strict=True: excludes boundary
    strict=False: includes boundary
    """
    n = len(l)
    r = 0 if strict else 1
    
    if n < 3:
        return r and on_segment(l[0], l[-1], p)
    
    a = 1
    b = n - 1
    
    if side_of(l[0], l[a], l[b]) > 0:
        a, b = b, a
    
    if side_of(l[0], l[a], p) >= r or side_of(l[0], l[b], p) <= -r:
        return False
    
    while abs(a - b) > 1:
        c = (a + b) // 2
        if side_of(l[0], l[c], p) > 0:
            b = c
        else:
            a = c
    
    return sgn(l[a].cross(l[b], p)) < r

