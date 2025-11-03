"""
Author: Ulf Lundstrom
Date: 2009-03-21
License: CC0
Description:
Returns a vector with the vertices of a polygon with everything to the left of the line going from s to e cut away.
Status: tested but not extensively
"""

from typing import List
from .point import Point

def polygon_cut(poly: List[Point], s: Point, e: Point) -> List[Point]:
    """
    Cut polygon with line from s to e.
    Returns vertices of polygon with everything to the left of line cut away.
    """
    res = []
    
    for i in range(len(poly)):
        cur = poly[i]
        prev = poly[i - 1] if i else poly[-1]
        a = s.cross(e, cur)
        b = s.cross(e, prev)
        
        if (a < 0) != (b < 0):
            res.append(cur + (prev - cur) * (a / (a - b)))
        if a < 0:
            res.append(cur)
    
    return res

