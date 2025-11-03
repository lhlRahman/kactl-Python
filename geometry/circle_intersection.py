"""
Author: Simon Lindholm
Date: 2015-09-01
License: CC0
Description: Computes the pair of points at which two circles intersect.
Returns None in case of no intersection.
Status: stress-tested
"""

import math
from typing import Optional, Tuple
from .point import Point

def circle_intersection(a: Point, b: Point, r1: float, r2: float) -> Optional[Tuple[Point, Point]]:
    """
    Find intersection points of two circles.
    a, b = centers of circles
    r1, r2 = radii
    Returns (point1, point2) or None if no intersection
    """
    if a == b:
        assert r1 != r2
        return None
    
    vec = b - a
    d2 = vec.dist2()
    sum_r = r1 + r2
    dif_r = r1 - r2
    
    if sum_r * sum_r < d2 or dif_r * dif_r > d2:
        return None
    
    p = (d2 + r1 * r1 - r2 * r2) / (d2 * 2)
    h2 = r1 * r1 - p * p * d2
    
    mid = a + vec * p
    per = vec.perp() * math.sqrt(max(0, h2) / d2)
    
    return (mid + per, mid - per)

