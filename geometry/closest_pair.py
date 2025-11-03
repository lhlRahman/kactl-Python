"""
Author: Simon Lindholm
Date: 2019-04-17
License: CC0
Source: https://codeforces.com/blog/entry/58747
Description: Finds the closest pair of points.
Time: O(n log n)
Status: stress-tested
"""

import math
from typing import List, Tuple
from .point import Point

def closest_pair(v: List[Point]) -> Tuple[Point, Point]:
    """
    Find the closest pair of points.
    Returns (point1, point2)
    """
    assert len(v) > 1
    
    S = set()
    v = sorted(v, key=lambda p: p.y)
    
    ret_dist2 = float('inf')
    ret_points = (Point(0, 0), Point(0, 0))
    j = 0
    
    for p in v:
        d_x = 1 + int(math.sqrt(ret_dist2))
        
        # Remove points that are too far below
        while v[j].y <= p.y - d_x:
            S.discard((v[j].x, v[j].y))
            j += 1
        
        # Check nearby points
        for x, y in sorted(S):
            q = Point(x, y)
            if abs(q.x - p.x) <= d_x and abs(q.y - p.y) <= d_x:
                dist2 = (q - p).dist2()
                if dist2 < ret_dist2:
                    ret_dist2 = dist2
                    ret_points = (q, p)
        
        S.add((p.x, p.y))
    
    return ret_points

