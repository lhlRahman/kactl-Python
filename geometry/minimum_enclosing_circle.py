"""
Author: Andrew He, chilli
Date: 2019-05-07
License: CC0
Source: folklore
Description: Computes the minimum circle that encloses a set of points.
Time: expected O(n)
Status: stress-tested
"""

import random
from typing import List, Tuple
from .point import Point
from .circumcircle import cc_center

def minimum_enclosing_circle(ps: List[Point]) -> Tuple[Point, float]:
    """
    Find minimum enclosing circle for a set of points.
    Returns (center, radius)
    """
    ps = ps[:]
    random.shuffle(ps)
    
    o = ps[0]
    r = 0.0
    EPS = 1 + 1e-8
    
    for i in range(len(ps)):
        if (o - ps[i]).dist() > r * EPS:
            o = ps[i]
            r = 0.0
            for j in range(i):
                if (o - ps[j]).dist() > r * EPS:
                    o = (ps[i] + ps[j]) / 2
                    r = (o - ps[i]).dist()
                    for k in range(j):
                        if (o - ps[k]).dist() > r * EPS:
                            o = cc_center(ps[i], ps[j], ps[k])
                            r = (o - ps[i]).dist()
    
    return (o, r)

