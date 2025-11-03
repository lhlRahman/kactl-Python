"""
Author: Mattias de Zalenski
Date: Unknown
Source: Geometry in C
Description: Computes the Delaunay triangulation of a set of points.
Each circumcircle contains none of the input points.
If any three points are collinear or any four are on the same circle,
behavior is undefined.
Time: O(n^2)
Status: stress-tested
"""

from typing import List, Callable
from .point import Point
from .point_3d import Point3D
from .hull_3d import hull_3d

def delaunay_triangulation(ps: List[Point], trifun: Callable[[int, int, int], None]):
    """
    Compute Delaunay triangulation and call trifun for each triangle.
    ps = list of 2D points
    trifun = callback function(a, b, c) for each triangle with vertices a,b,c
    """
    n = len(ps)
    
    if n == 3:
        # Special case: exactly 3 points
        d = 1 if ps[0].cross(ps[1], ps[2]) < 0 else 0
        trifun(0, 1 + d, 2 - d)
        return
    
    if n < 3:
        return
    
    # Lift points to paraboloid: (x, y) -> (x, y, x^2 + y^2)
    p3 = []
    for p in ps:
        p3.append(Point3D(p.x, p.y, p.dist2()))
    
    # Compute 3D convex hull
    if n > 3:
        faces = hull_3d(p3)
        
        # Extract lower hull faces (those visible from below, z = -infinity)
        for face in faces:
            v1 = p3[face.b] - p3[face.a]
            v2 = p3[face.c] - p3[face.a]
            normal = v1.cross(v2)
            
            # If normal points down (negative z component), it's part of lower hull
            if normal.z < 0:
                trifun(face.a, face.c, face.b)

def get_delaunay_triangles(ps: List[Point]) -> List[tuple]:
    """
    Compute Delaunay triangulation and return list of triangles.
    ps = list of 2D points
    Returns list of (a, b, c) tuples representing triangle vertex indices
    """
    triangles = []
    delaunay_triangulation(ps, lambda a, b, c: triangles.append((a, b, c)))
    return triangles

