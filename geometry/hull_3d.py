"""
Author: Johan Sannemo
Date: 2017-04-18
Source: derived from https://gist.github.com/msg555/4963794 by Mark Gordon
Description: Computes all faces of the 3-dimension hull of a point set.
*No four points must be coplanar*, or else random results will be returned.
All faces will point outwards.
Time: O(n^2)
Status: tested on SPOJ CH3D
"""

from typing import List, Tuple
from .point_3d import Point3D

class Face:
    def __init__(self, q: Point3D, a: int, b: int, c: int):
        self.q = q  # Normal vector
        self.a = a  # Vertex indices
        self.b = b
        self.c = c

def hull_3d(A: List[Point3D]) -> List[Face]:
    """
    Compute 3D convex hull.
    A = list of 3D points (at least 4, no 4 coplanar)
    Returns list of Face objects
    """
    assert len(A) >= 4, "Need at least 4 points"
    
    n = len(A)
    # E[i][j] = pair of faces adjacent to edge i-j
    E = [[[-1, -1] for _ in range(n)] for _ in range(n)]
    
    def E_ins(i, j, x):
        """Insert face x into edge i-j"""
        if E[i][j][0] == -1:
            E[i][j][0] = x
        else:
            E[i][j][1] = x
    
    def E_rem(i, j, x):
        """Remove face x from edge i-j"""
        if E[i][j][0] == x:
            E[i][j][0] = -1
        else:
            E[i][j][1] = -1
    
    def E_cnt(i, j):
        """Count faces on edge i-j"""
        return (E[i][j][0] != -1) + (E[i][j][1] != -1)
    
    FS = []  # List of faces
    
    def make_face(i, j, k, l):
        """Create face from points i, j, k with l as reference"""
        q = (A[j] - A[i]).cross(A[k] - A[i])
        if q.dot(A[l]) > q.dot(A[i]):
            q = q * -1
        
        f = Face(q, i, j, k)
        E_ins(i, j, k)
        E_ins(i, k, j)
        E_ins(j, k, i)
        FS.append(f)
    
    # Create initial tetrahedron
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                make_face(i, j, k, 6 - i - j - k)
    
    # Add remaining points incrementally
    for i in range(4, n):
        j = 0
        while j < len(FS):
            f = FS[j]
            if f.q.dot(A[i]) > f.q.dot(A[f.a]):
                # Remove face visible from new point
                E_rem(f.a, f.b, f.c)
                E_rem(f.a, f.c, f.b)
                E_rem(f.b, f.c, f.a)
                FS[j] = FS[-1]
                FS.pop()
                j -= 1
            j += 1
        
        # Add new faces
        nw = len(FS)
        for j in range(nw):
            f = FS[j]
            if E_cnt(f.a, f.b) != 2:
                make_face(f.a, f.b, i, f.c)
            if E_cnt(f.a, f.c) != 2:
                make_face(f.a, f.c, i, f.b)
            if E_cnt(f.b, f.c) != 2:
                make_face(f.b, f.c, i, f.a)
    
    # Ensure correct orientation
    for f in FS:
        if (A[f.b] - A[f.a]).cross(A[f.c] - A[f.a]).dot(f.q) <= 0:
            f.b, f.c = f.c, f.b
    
    return FS

