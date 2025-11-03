"""
Author: Mattias de Zalenski
Date: 2002-11-04
Description: Magic formula for the volume of a polyhedron. Faces should point outwards.
Status: tested
"""

from typing import List, Any
from .point_3d import Point3D

def signed_poly_volume(p: List[Point3D], trilist: List[Any]) -> float:
    """
    Calculate volume of polyhedron.
    p = list of 3D points
    trilist = list of triangles (each with attributes a, b, c as indices into p)
    """
    v = 0.0
    for tri in trilist:
        v += p[tri.a].cross(p[tri.b]).dot(p[tri.c])
    return v / 6

