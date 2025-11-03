"""
Author: Ulf Lundstrom
Date: 2009-03-21
License: CC0
Source: Basic math
Description:
Returns the signed distance between point p and the line containing points a and b.
Positive value on left side and negative on right as seen from a towards b. a==b gives nan.
It uses products in intermediate steps so watch out for overflow.
Status: tested
"""

from .point import Point

def line_dist(a: Point, b: Point, p: Point) -> float:
    """
    Signed distance from point p to line through a and b.
    Positive on left, negative on right (as seen from a to b).
    """
    return (b - a).cross(p - a) / (b - a).dist()

