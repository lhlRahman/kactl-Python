"""
Author: Victor Lecomte, chilli
Date: 2019-04-27
License: CC0
Source: https://vlecomte.github.io/cp-geo.pdf
Description:
If a unique intersection point between the line segments going from s1 to e1 and from s2 to e2 exists then it is returned.
If no intersection point exists an empty list is returned.
If infinitely many exist a list with 2 elements is returned, containing the endpoints of the common line segment.
Status: stress-tested, tested on kattis:intersection
"""

from typing import List
from .point import Point
from .on_segment import on_segment
from .side_of import sgn

def segment_intersection(a: Point, b: Point, c: Point, d: Point) -> List[Point]:
    """
    Find intersection of line segments ab and cd.
    Returns list of intersection points (0, 1, or 2 points).
    """
    oa = c.cross(d, a)
    ob = c.cross(d, b)
    oc = a.cross(b, c)
    od = a.cross(b, d)
    
    # Check if intersection is single non-endpoint point
    if sgn(oa) * sgn(ob) < 0 and sgn(oc) * sgn(od) < 0:
        return [(a * ob - b * oa) / (ob - oa)]
    
    # Check endpoints
    s = set()
    if on_segment(c, d, a):
        s.add((a.x, a.y))
    if on_segment(c, d, b):
        s.add((b.x, b.y))
    if on_segment(a, b, c):
        s.add((c.x, c.y))
    if on_segment(a, b, d):
        s.add((d.x, d.y))
    
    return [Point(x, y) for x, y in sorted(s)]

