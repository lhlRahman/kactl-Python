"""
Author: Victor Lecomte, chilli
Date: 2019-05-05
License: CC0
Source: https://vlecomte.github.io/cp-geo.pdf
Description:
If a unique intersection point of the lines going through s1,e1 and s2,e2 exists {1, point} is returned.
If no intersection point exists {0, (0,0)} is returned and if infinitely many exists {-1, (0,0)} is returned.
The wrong position will be returned if P is Point with integer coordinates and the intersection point does not have integer coordinates.
Products of three coordinates are used in intermediate steps so watch out for overflow.
Status: stress-tested, and tested through half-plane tests
"""

from typing import Tuple
from .point import Point

def line_intersection(s1: Point, e1: Point, s2: Point, e2: Point) -> Tuple[int, Point]:
    """
    Find intersection of two lines.
    Returns (status, point) where:
      status = 1: unique intersection at point
      status = 0: no intersection (parallel lines)
      status = -1: infinitely many intersections (same line)
    """
    d = (e1 - s1).cross(e2 - s2)
    if d == 0:  # parallel
        status = -1 if s1.cross(e1, s2) == 0 else 0
        return (status, Point(0, 0))
    
    p = s2.cross(e1, e2)
    q = s2.cross(e2, s1)
    return (1, (s1 * p + e1 * q) / d)

