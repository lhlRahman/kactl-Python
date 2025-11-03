"""
Author: Ulf Lundstrom with inspiration from tinyKACTL
Date: 2009-04-14
License: CC0
Description: Class to handle points in 3D space.
Usage:
Status: tested, except for phi and theta
"""

import math
from typing import Tuple

class Point3D:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __lt__(self, p: 'Point3D') -> bool:
        return (self.x, self.y, self.z) < (p.x, p.y, p.z)
    
    def __eq__(self, p: 'Point3D') -> bool:
        return (self.x, self.y, self.z) == (p.x, p.y, p.z)
    
    def __add__(self, p: 'Point3D') -> 'Point3D':
        return Point3D(self.x + p.x, self.y + p.y, self.z + p.z)
    
    def __sub__(self, p: 'Point3D') -> 'Point3D':
        return Point3D(self.x - p.x, self.y - p.y, self.z - p.z)
    
    def __mul__(self, d: float) -> 'Point3D':
        return Point3D(self.x * d, self.y * d, self.z * d)
    
    def __truediv__(self, d: float) -> 'Point3D':
        return Point3D(self.x / d, self.y / d, self.z / d)
    
    def dot(self, p: 'Point3D') -> float:
        """Dot product"""
        return self.x * p.x + self.y * p.y + self.z * p.z
    
    def cross(self, p: 'Point3D') -> 'Point3D':
        """Cross product"""
        return Point3D(
            self.y * p.z - self.z * p.y,
            self.z * p.x - self.x * p.z,
            self.x * p.y - self.y * p.x
        )
    
    def dist2(self) -> float:
        """Squared distance from origin"""
        return self.x * self.x + self.y * self.y + self.z * self.z
    
    def dist(self) -> float:
        """Distance from origin"""
        return math.sqrt(self.dist2())
    
    def phi(self) -> float:
        """Azimuthal angle (longitude) to x-axis in interval [-pi, pi]"""
        return math.atan2(self.y, self.x)
    
    def theta(self) -> float:
        """Zenith angle (latitude) to the z-axis in interval [0, pi]"""
        return math.atan2(math.sqrt(self.x * self.x + self.y * self.y), self.z)
    
    def unit(self) -> 'Point3D':
        """Unit vector (makes dist() = 1)"""
        return self / self.dist()
    
    def normal(self, p: 'Point3D') -> 'Point3D':
        """Unit vector normal to self and p"""
        return self.cross(p).unit()
    
    def rotate(self, angle: float, axis: 'Point3D') -> 'Point3D':
        """Rotate 'angle' radians ccw around axis"""
        s = math.sin(angle)
        c = math.cos(angle)
        u = axis.unit()
        return u * self.dot(u) * (1 - c) + self * c - self.cross(u) * s
    
    def __repr__(self) -> str:
        return f"Point3D({self.x}, {self.y}, {self.z})"

