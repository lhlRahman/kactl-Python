"""
Author: Lukas Polacek
Date: 2009-10-26
License: CC0
Source: folklore
Description: Disjoint-set data structure.
Time: O(α(N))
"""

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.e = [-1] * n
    
    def same_set(self, a: int, b: int) -> bool:
        """Check if a and b are in the same set"""
        return self.find(a) == self.find(b)
    
    def size(self, x: int) -> int:
        """Get size of set containing x"""
        return -self.e[self.find(x)]
    
    def find(self, x: int) -> int:
        """Find representative of set containing x"""
        if self.e[x] < 0:
            return x
        self.e[x] = self.find(self.e[x])
        return self.e[x]
    
    def join(self, a: int, b: int) -> bool:
        """Join sets containing a and b. Returns True if they were different sets."""
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.e[a] > self.e[b]:
            a, b = b, a
        self.e[a] += self.e[b]
        self.e[b] = a
        return True
