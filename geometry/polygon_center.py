"""
Author: Ulf Lundstrom
Date: 2009-04-08
License: CC0
Description: Returns the center of mass for a polygon.
Time: O(n)
Status: Tested
"""

from typing import List
from .point import Point

def polygon_center(v: List[Point]) -> Point:
    """Calculate center of mass of polygon"""
    res = Point(0, 0)
    A = 0.0
    
    j = len(v) - 1
    for i in range(len(v)):
        res = res + (v[i] + v[j]) * v[j].cross(v[i])
        A += v[j].cross(v[i])
        j = i
    
    return res / A / 3

