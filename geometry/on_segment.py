"""
Author: Victor Lecomte, chilli
Date: 2019-04-26
License: CC0
Source: https://vlecomte.github.io/cp-geo.pdf
Description: Returns true iff p lies on the line segment from s to e.
Use (seg_dist(s,e,p)<=epsilon) instead when using floating point.
Status: tested
"""

from .point import Point

def on_segment(s: Point, e: Point, p: Point) -> bool:
    """Check if point p lies on line segment from s to e"""
    return p.cross(s, e) == 0 and (s - p).dot(e - p) <= 0

