"""
Author: Victor Lecomte, chilli
Date: 2019-10-29
License: CC0
Source: https://vlecomte.github.io/cp-geo.pdf
Description: Projects point p onto line ab. Set refl=True to get reflection
of point p across line ab instead.
Products of three coordinates are used in intermediate steps so watch out for overflow.
Status: stress-tested
"""

from .point import Point

def line_proj(a: Point, b: Point, p: Point, refl: bool = False) -> Point:
    """
    Project point p onto line through a and b.
    If refl=True, returns reflection instead of projection.
    """
    v = b - a
    return p - v.perp() * (1 + refl) * v.cross(p - a) / v.dist2()

