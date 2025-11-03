"""
Author: Oleksandr Bacherikov, chilli
Date: 2019-05-05
License: Boost Software License
Source: https://codeforces.com/blog/entry/48868
Description: Returns the two points with max distance on a convex hull (ccw,
no duplicate/collinear points).
Status: stress-tested, tested on kattis:roberthood
Time: O(n)
"""

from typing import List, Tuple
from .point import Point

def hull_diameter(S: List[Point]) -> Tuple[Point, Point]:
    """
    Find diameter of convex hull (furthest pair of points).
    Hull must be CCW with no duplicates or collinear points.
    Returns (point1, point2)
    """
    n = len(S)
    if n < 2:
        return (S[0], S[0])
    
    j = 1
    res_dist2 = 0
    res_points = (S[0], S[0])
    
    for i in range(j):
        while True:
            dist2 = (S[i] - S[j]).dist2()
            if dist2 > res_dist2:
                res_dist2 = dist2
                res_points = (S[i], S[j])
            
            if (S[(j + 1) % n] - S[j]).cross(S[i + 1] - S[i]) >= 0:
                break
            j = (j + 1) % n
    
    return res_points

