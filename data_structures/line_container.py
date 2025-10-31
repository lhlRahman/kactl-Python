"""
Author: Simon Lindholm
Date: 2017-04-20
License: CC0
Source: own work
Description: Container where you can add lines of the form kx+m, and query maximum values at points x.
Useful for dynamic programming ("convex hull trick").
Time: O(log N)
Status: stress-tested
"""

from sortedcontainers import SortedList
from typing import Optional

class Line:
    def __init__(self, k: int, m: int, p: int = 0):
        self.k = k
        self.m = m
        self.p = p  # intersection point with next line
    
    def __lt__(self, other):
        if isinstance(other, Line):
            return self.k < other.k
        else:
            return self.p < other

class LineContainer:
    """Container for convex hull trick"""
    INF = 10**18
    
    def __init__(self):
        self.lines = SortedList(key=lambda x: x.k)
    
    def div(self, a: int, b: int) -> int:
        """Floored division"""
        return a // b - (1 if (a ^ b) < 0 and a % b else 0)
    
    def isect(self, x: Line, y: Optional[Line]) -> bool:
        """Update intersection point and check if x should be removed"""
        if y is None:
            x.p = self.INF
            return False
        if x.k == y.k:
            x.p = self.INF if x.m > y.m else -self.INF
        else:
            x.p = self.div(y.m - x.m, x.k - y.k)
        return x.p >= y.p
    
    def add(self, k: int, m: int):
        """Add line kx + m"""
        new_line = Line(k, m)
        idx = self.lines.bisect_left(new_line)
        self.lines.add(new_line)
        
        # Update intersections
        y_idx = idx + 1
        if y_idx < len(self.lines):
            y = self.lines[y_idx]
            while self.isect(new_line, y if y_idx < len(self.lines) else None):
                if y_idx < len(self.lines):
                    self.lines.pop(y_idx)
                    if y_idx < len(self.lines):
                        y = self.lines[y_idx]
                    else:
                        break
                else:
                    break
        
        # Update with previous line
        if idx > 0:
            x = self.lines[idx - 1]
            if self.isect(x, new_line):
                self.lines.pop(idx)
                self.isect(x, self.lines[idx] if idx < len(self.lines) else None)
        
        # Clean up previous lines
        while idx > 1:
            x = self.lines[idx - 2]
            y = self.lines[idx - 1]
            if x.p >= y.p:
                self.lines.pop(idx - 1)
                idx -= 1
                self.isect(x, self.lines[idx - 1] if idx - 1 < len(self.lines) else None)
            else:
                break
    
    def query(self, x: int) -> int:
        """Query maximum value at point x"""
        assert len(self.lines) > 0
        # Binary search for the right line
        idx = 0
        for i, line in enumerate(self.lines):
            if line.p >= x:
                idx = i
                break
        l = self.lines[idx]
        return l.k * x + l.m

