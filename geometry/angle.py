"""
Author: Simon Lindholm
Date: 2015-01-31
License: CC0
Source: me
Description: A class for ordering angles (as represented by int points and
a number of rotations around the origin). Useful for rotational sweeping.
Sometimes also represents points or vectors.
Status: Used, works well
"""

from typing import Tuple

class Angle:
    def __init__(self, x: int, y: int, t: int = 0):
        self.x = x
        self.y = y
        self.t = t  # number of rotations
    
    def __sub__(self, b: 'Angle') -> 'Angle':
        return Angle(self.x - b.x, self.y - b.y, self.t)
    
    def half(self) -> int:
        """Which half-plane is this angle in?"""
        assert self.x or self.y
        return 1 if self.y < 0 or (self.y == 0 and self.x < 0) else 0
    
    def t90(self) -> 'Angle':
        """Rotate 90 degrees"""
        return Angle(-self.y, self.x, self.t + (1 if self.half() and self.x >= 0 else 0))
    
    def t180(self) -> 'Angle':
        """Rotate 180 degrees"""
        return Angle(-self.x, -self.y, self.t + self.half())
    
    def t360(self) -> 'Angle':
        """Rotate 360 degrees"""
        return Angle(self.x, self.y, self.t + 1)
    
    def __lt__(self, b: 'Angle') -> bool:
        return (self.t, self.half(), self.y * b.x) < (b.t, b.half(), self.x * b.y)
    
    def __add__(self, b: 'Angle') -> 'Angle':
        """Add point a + vector b"""
        r = Angle(self.x + b.x, self.y + b.y, self.t)
        if self.t180() < r:
            r.t -= 1
        return r.t360() if r.t180() < self else r
    
    def dist2(self) -> int:
        """Squared distance from origin"""
        return self.x * self.x + self.y * self.y

def segment_angles(a: Angle, b: Angle) -> Tuple[Angle, Angle]:
    """
    Given two points, calculate the smallest angle between them,
    i.e., the angle that covers the defined line segment.
    """
    if b < a:
        a, b = b, a
    if b < a.t180():
        return (a, b)
    else:
        return (b, a.t360())

def angle_diff(a: Angle, b: Angle) -> Angle:
    """Angle b - angle a"""
    tu = b.t - a.t
    a.t = b.t
    return Angle(a.x * b.x + a.y * b.y, a.x * b.y - a.y * b.x, tu - (1 if b < a else 0))

