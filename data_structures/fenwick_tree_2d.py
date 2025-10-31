"""
Author: Simon Lindholm
Date: 2017-05-11
License: CC0
Source: folklore
Description: Computes sums a[i,j] for all i<I, j<J, and increases single elements a[i,j].
Requires that the elements to be updated are known in advance (call fake_update() before init()).
Time: O(log^2 N). (Use persistent segment trees for O(log N).)
Status: stress-tested
"""

from typing import List
from bisect import bisect_left
from .fenwick_tree import FenwickTree

class FenwickTree2D:
    def __init__(self, limx: int):
        self.ys = [[] for _ in range(limx)]
        self.ft = []
    
    def fake_update(self, x: int, y: int):
        """Register that position (x, y) will be updated"""
        while x < len(self.ys):
            self.ys[x].append(y)
            x |= x + 1
    
    def init(self):
        """Initialize after all fake_update() calls"""
        for v in self.ys:
            v.sort()
            self.ft.append(FenwickTree(len(v)))
    
    def ind(self, x: int, y: int) -> int:
        """Find index of y in ys[x]"""
        return bisect_left(self.ys[x], y)
    
    def update(self, x: int, y: int, dif: int):
        """Add dif to position (x, y)"""
        while x < len(self.ys):
            self.ft[x].update(self.ind(x, y), dif)
            x |= x + 1
    
    def query(self, x: int, y: int) -> int:
        """Query sum of rectangle [0, x) x [0, y)"""
        total = 0
        while x:
            total += self.ft[x - 1].query(self.ind(x - 1, y))
            x &= x - 1
        return total

