"""
Author: Victor Lecomte, chilli
Date: 2019-10-31
License: CC0
Source: https://vlecomte.github.io/cp-geo.pdf
Description: Finds the external tangents of two circles, or internal if r2 is negated.
Can return 0, 1, or 2 tangents.
.first and .second give the tangency points at circle 1 and 2 respectively.
To find the tangents of a circle with a point set r2 to 0.
Status: tested
"""

import math
from typing import List, Tuple
from .point import Point

def circle_tangents(c1: Point, r1: float, c2: Point, r2: float) -> List[Tuple[Point, Point]]:
    """
    Find tangent lines of two circles.
    Returns list of (point_on_c1, point_on_c2) pairs.
    For internal tangents, negate r2.
    For tangents from point to circle, set r2=0.
    """
    d = c2 - c1
    dr = r1 - r2
    d2 = d.dist2()
    h2 = d2 - dr * dr
    
    if d2 == 0 or h2 < 0:
        return []
    
    out = []
    for sign in [-1, 1]:
        v = (d * dr + d.perp() * math.sqrt(h2) * sign) / d2
        out.append((c1 + v * r1, c2 + v * r2))
    
    if h2 == 0:
        out.pop()
    
    return out

