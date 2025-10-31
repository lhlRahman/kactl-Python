"""
Author: Lukas Polacek, Simon Lindholm
Date: 2019-12-26
License: CC0
Source: folklore
Description: Disjoint-set data structure with undo.
If undo is not needed, skip st, time() and rollback().
Usage: t = uf.time(); ...; uf.rollback(t);
Time: O(log(N))
Status: tested as part of DirectedMST.h
"""

from typing import List, Tuple

class UnionFindRollback:
    def __init__(self, n: int):
        self.e = [-1] * n
        self.st: List[Tuple[int, int]] = []
    
    def size(self, x: int) -> int:
        """Get size of set containing x"""
        return -self.e[self.find(x)]
    
    def find(self, x: int) -> int:
        """Find representative of set containing x (no path compression)"""
        return x if self.e[x] < 0 else self.find(self.e[x])
    
    def time(self) -> int:
        """Get current time for rollback"""
        return len(self.st)
    
    def rollback(self, t: int):
        """Rollback to time t"""
        while len(self.st) > t:
            idx, val = self.st.pop()
            self.e[idx] = val
    
    def join(self, a: int, b: int) -> bool:
        """Join sets containing a and b. Returns True if they were different sets."""
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.e[a] > self.e[b]:
            a, b = b, a
        self.st.append((a, self.e[a]))
        self.st.append((b, self.e[b]))
        self.e[a] += self.e[b]
        self.e[b] = a
        return True

