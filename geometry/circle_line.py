"""
Author: Victor Lecomte, chilli
Date: 2019-10-29
License: CC0
Source: https://vlecomte.github.io/cp-geo.pdf
Description: Finds the intersection between a circle and a line.
Returns a list of either 0, 1, or 2 intersection points.
Status: unit tested
"""

import math
from typing import List
from .point import Point

def circle_line(c: Point, r: float, a: Point, b: Point) -> List[Point]:
    """
    Find intersection of circle with center c and radius r with line through a and b.
    Returns list of intersection points (0, 1, or 2 points).
    """
    ab = b - a
    p = a + ab * (c - a).dot(ab) / ab.dist2()
    s = a.cross(b, c)
    h2 = r * r - s * s / ab.dist2()
    
    if h2 < 0:
        return []
    if h2 == 0:
        return [p]
    
    h = ab.unit() * math.sqrt(h2)
    return [p - h, p + h]

