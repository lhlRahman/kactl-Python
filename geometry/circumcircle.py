"""
Author: Ulf Lundstrom
Date: 2009-04-11
License: CC0
Source: http://en.wikipedia.org/wiki/Circumcircle
Description:
The circumcircle of a triangle is the circle intersecting all three vertices.
cc_radius returns the radius and cc_center returns the center.
Status: tested
"""

from .point import Point

def cc_radius(A: Point, B: Point, C: Point) -> float:
    """Calculate radius of circumcircle of triangle ABC"""
    return ((B - A).dist() * (C - B).dist() * (A - C).dist() / 
            abs((B - A).cross(C - A)) / 2)

def cc_center(A: Point, B: Point, C: Point) -> Point:
    """Calculate center of circumcircle of triangle ABC"""
    b = C - A
    c = B - A
    return A + (b * c.dist2() - c * b.dist2()).perp() / b.cross(c) / 2

