"""
Author: Ulf Lundstrom
Date: 2009-04-07
License: CC0
Source: My geometric reasoning
Description: Returns the shortest distance on the sphere with radius between points
with azimuthal angles (longitude) f1, f2 from x axis and zenith angles
(latitude) t1, t2 from z axis (0 = north pole). All angles in radians.
Status: tested on kattis:airlinehub
"""

import math

def spherical_distance(f1: float, t1: float, f2: float, t2: float, radius: float) -> float:
    """
    Calculate shortest distance on sphere between two points.
    f1, f2 = azimuthal angles (longitude) in radians
    t1, t2 = zenith angles (latitude) in radians (0 = north pole)
    radius = sphere radius
    """
    dx = math.sin(t2) * math.cos(f2) - math.sin(t1) * math.cos(f1)
    dy = math.sin(t2) * math.sin(f2) - math.sin(t1) * math.sin(f1)
    dz = math.cos(t2) - math.cos(t1)
    d = math.sqrt(dx * dx + dy * dy + dz * dz)
    return radius * 2 * math.asin(d / 2)

