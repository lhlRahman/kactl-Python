"""
Author: Per Austrin, Ulf Lundstrom
Date: 2009-04-09
License: CC0
Description: Apply the linear transformation (translation, rotation and scaling)
which takes line p0-p1 to line q0-q1 to point r.
Status: not tested
"""

from .point import Point

def linear_transformation(p0: Point, p1: Point, q0: Point, q1: Point, r: Point) -> Point:
    """
    Transform point r by the linear transformation that maps line p0-p1 to q0-q1.
    p0, p1 = source line endpoints
    q0, q1 = destination line endpoints
    r = point to transform
    Returns transformed point
    """
    dp = p1 - p0
    dq = q1 - q0
    
    # Compute complex number representing transformation
    num = Point(dp.cross(dq), dp.dot(dq))
    
    # Apply transformation
    r_rel = r - p0
    transformed = Point(r_rel.cross(num), r_rel.dot(num))
    
    return q0 + transformed / dp.dist2()

# Example usage
if __name__ == "__main__":
    # Transform a point from one coordinate system to another
    p0 = Point(0.0, 0.0)
    p1 = Point(1.0, 0.0)
    q0 = Point(0.0, 0.0)
    q1 = Point(0.0, 1.0)  # 90 degree rotation
    r = Point(0.5, 0.0)
    
    result = linear_transformation(p0, p1, q0, q1, r)
    print(f"Transformed point: ({result.x}, {result.y})")
