"""
Author: black_horse2014, chilli
Date: 2019-10-29
License: Unknown
Source: https://codeforces.com/gym/101673/submission/50481926
Description: Calculates the area of the union of n polygons (not necessarily
convex). The points within each polygon must be given in CCW order.
Time: O(N^2), where N is the total number of points
Status: stress-tested, Submitted on ECNA 2017 Problem A
"""

from typing import List
from .point import Point
from .side_of import side_of, sgn

def rat(a: Point, b: Point) -> float:
    """Ratio helper function"""
    return a.x / b.x if sgn(b.x) else a.y / b.y

def polygon_union(poly: List[List[Point]]) -> float:
    """
    Calculate area of union of polygons.
    poly = list of polygons (each polygon is a list of points in CCW order)
    """
    ret = 0.0
    
    for i in range(len(poly)):
        for v in range(len(poly[i])):
            A = poly[i][v]
            B = poly[i][(v + 1) % len(poly[i])]
            segs = [(0.0, 0), (1.0, 0)]
            
            for j in range(len(poly)):
                if i != j:
                    for u in range(len(poly[j])):
                        C = poly[j][u]
                        D = poly[j][(u + 1) % len(poly[j])]
                        sc = side_of(A, B, C)
                        sd = side_of(A, B, D)
                        
                        if sc != sd:
                            sa = C.cross(D, A)
                            sb = C.cross(D, B)
                            if min(sc, sd) < 0:
                                segs.append((sa / (sa - sb), sgn(sc - sd)))
                        elif not sc and not sd and j < i and sgn((B - A).dot(D - C)) > 0:
                            segs.append((rat(C - A, B - A), 1))
                            segs.append((rat(D - A, B - A), -1))
            
            segs.sort()
            for k in range(len(segs)):
                segs[k] = (min(max(segs[k][0], 0.0), 1.0), segs[k][1])
            
            total = 0.0
            cnt = segs[0][1]
            for j in range(1, len(segs)):
                if not cnt:
                    total += segs[j][0] - segs[j - 1][0]
                cnt += segs[j][1]
            
            ret += A.cross(B) * total
    
    return ret / 2

