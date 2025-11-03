"""
Author: Ulf Lundstrom
Date: 2009-03-21
License: CC0
Description: Returns where p is as seen from s towards e. 1/0/-1 <=> left/on line/right.
If the optional argument eps is given 0 is returned if p is within distance eps from the line.
It uses products in intermediate steps so watch out for overflow.
Status: tested
"""

from .point import Point

def sgn(x: float) -> int:
    """Sign function"""
    return (x > 0) - (x < 0)

def side_of(s: Point, e: Point, p: Point, eps: float = None) -> int:
    """
    Check which side of line (s->e) point p is on.
    Returns 1 (left), 0 (on line), -1 (right)
    If eps is given, returns 0 if p is within distance eps from line
    """
    if eps is None:
        return sgn(s.cross(e, p))
    else:
        a = (e - s).cross(p - s)
        l = (e - s).dist() * eps
        return (1 if a > l else 0) - (1 if a < -l else 0)

