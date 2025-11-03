"""
Author: Ulf Lundstrom
Date: 2009-03-21
License: CC0
Description:
Returns the shortest distance between point p and the line segment from point s to e.
Status: tested
"""

from .point import Point

def segment_dist(s: Point, e: Point, p: Point) -> float:
    """
    Shortest distance from point p to line segment from s to e.
    """
    if s == e:
        return (p - s).dist()
    d = (e - s).dist2()
    t = min(d, max(0.0, (p - s).dot(e - s)))
    return ((p - s) * d - (e - s) * t).dist() / d

