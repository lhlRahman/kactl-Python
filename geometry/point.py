"""
Author: Ulf Lundstrom
Date: 2009-02-26
License: CC0
Source: My head with inspiration from tinyKACTL
Description: Class to handle points in the plane.
Status: Works fine, used a lot
"""

import math
from typing import Tuple

def sgn(x):
    """Return sign of x: 1 if positive, -1 if negative, 0 if zero"""
    return (x > 0) - (x < 0)

class Point:
    """2D Point class"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __lt__(self, p):
        return (self.x, self.y) < (p.x, p.y)
    
    def __eq__(self, p):
        return (self.x, self.y) == (p.x, p.y)
    
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    
    def __mul__(self, d):
        return Point(self.x * d, self.y * d)
    
    def __truediv__(self, d):
        return Point(self.x / d, self.y / d)
    
    def dot(self, p):
        """Dot product"""
        return self.x * p.x + self.y * p.y
    
    def cross(self, p, b=None):
        """Cross product. If b is given, compute cross product of vectors (p-self) and (b-self)"""
        if b is None:
            return self.x * p.y - self.y * p.x
        else:
            return (p - self).cross(b - self)
    
    def dist2(self):
        """Squared distance from origin"""
        return self.x * self.x + self.y * self.y
    
    def dist(self):
        """Distance from origin"""
        return math.sqrt(self.dist2())
    
    def angle(self):
        """Angle to x-axis in interval [-pi, pi]"""
        return math.atan2(self.y, self.x)
    
    def unit(self):
        """Return unit vector in same direction"""
        return self / self.dist()
    
    def perp(self):
        """Rotate 90 degrees counter-clockwise"""
        return Point(-self.y, self.x)
    
    def normal(self):
        """Return unit normal vector"""
        return self.perp().unit()
    
    def rotate(self, a):
        """Rotate 'a' radians counter-clockwise around origin"""
        return Point(self.x * math.cos(a) - self.y * math.sin(a),
                    self.x * math.sin(a) + self.y * math.cos(a))
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __repr__(self):
        return str(self)
    
    def __hash__(self):
        return hash((self.x, self.y))

