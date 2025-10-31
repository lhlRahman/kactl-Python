"""
Author: Lucian Bicsi
Date: 2017-10-31
License: CC0
Source: folklore
Description: Zero-indexed max-tree. Bounds are inclusive to the left and exclusive to the right.
Can be changed by modifying T, f and unit.
Time: O(log N)
Status: stress-tested
"""

from typing import List, Callable, TypeVar

T = TypeVar('T')

class SegmentTree:
    def __init__(self, n: int, f: Callable[[T, T], T], unit: T, def_val: T = None):
        """
        Create segment tree with n elements.
        f = associative function to combine elements
        unit = identity element
        def_val = default value (defaults to unit)
        """
        self.n = n
        self.f = f
        self.unit = unit
        if def_val is None:
            def_val = unit
        self.s = [def_val] * (2 * n)
    
    def update(self, pos: int, val: T):
        """Update position pos to value val"""
        pos += self.n
        self.s[pos] = val
        while pos > 1:
            pos //= 2
            self.s[pos] = self.f(self.s[pos * 2], self.s[pos * 2 + 1])
    
    def query(self, b: int, e: int) -> T:
        """Query range [b, e)"""
        ra = self.unit
        rb = self.unit
        b += self.n
        e += self.n
        while b < e:
            if b % 2:
                ra = self.f(ra, self.s[b])
                b += 1
            if e % 2:
                e -= 1
                rb = self.f(self.s[e], rb)
            b //= 2
            e //= 2
        return self.f(ra, rb)

# Example usage for max tree:
def create_max_tree(n: int) -> SegmentTree:
    """Create a max segment tree"""
    return SegmentTree(n, max, float('-inf'))

# Example usage for sum tree:
def create_sum_tree(n: int) -> SegmentTree:
    """Create a sum segment tree"""
    return SegmentTree(n, lambda a, b: a + b, 0)
