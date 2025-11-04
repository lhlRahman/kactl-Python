"""
Author: David Rydh, Per Austrin
Date: 2003-03-16
Description: Basic polynomial operations.
"""

from typing import List

class Polynomial:
    def __init__(self, a: List[float]):
        self.a = a[:]
    
    def __call__(self, x: float) -> float:
        """Evaluate polynomial at x using Horner's method"""
        val = 0.0
        for i in range(len(self.a) - 1, -1, -1):
            val = val * x + self.a[i]
        return val
    
    def diff(self):
        """Differentiate polynomial in-place"""
        for i in range(1, len(self.a)):
            self.a[i - 1] = i * self.a[i]
        if self.a:
            self.a.pop()
    
    def divroot(self, x0: float):
        """Divide polynomial by (x - x0) using synthetic division"""
        if not self.a:
            return
        b = self.a[-1]
        self.a[-1] = 0
        for i in range(len(self.a) - 2, -1, -1):
            c = self.a[i]
            self.a[i] = self.a[i + 1] * x0 + b
            b = c
        self.a.pop()

