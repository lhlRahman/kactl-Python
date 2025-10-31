"""
Author: Lukas Polacek
Date: 2009-10-30
License: CC0
Source: folklore/TopCoder
Description: Computes partial sums a[0] + a[1] + ... + a[pos - 1], and updates single elements a[i],
taking the difference between the old and new value.
Time: Both operations are O(log N).
Status: Stress-tested
"""

from typing import List

class FenwickTree:
    def __init__(self, n: int):
        self.s = [0] * n
    
    def update(self, pos: int, dif: int):
        """a[pos] += dif"""
        while pos < len(self.s):
            self.s[pos] += dif
            pos |= pos + 1
    
    def query(self, pos: int) -> int:
        """sum of values in [0, pos)"""
        res = 0
        while pos > 0:
            res += self.s[pos - 1]
            pos &= pos - 1
        return res
    
    def lower_bound(self, sum_val: int) -> int:
        """min pos st sum of [0, pos] >= sum_val
        Returns n if no sum is >= sum_val, or -1 if empty sum is."""
        if sum_val <= 0:
            return -1
        pos = 0
        pw = 1 << 25
        while pw:
            if pos + pw <= len(self.s) and self.s[pos + pw - 1] < sum_val:
                pos += pw
                sum_val -= self.s[pos - 1]
            pw >>= 1
        return pos

