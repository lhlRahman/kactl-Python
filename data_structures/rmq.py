"""
Author: Johan Sannemo, pajenegod
Date: 2015-02-06
License: CC0
Source: Folklore
Description: Range Minimum Queries on an array. Returns
min(V[a], V[a + 1], ... V[b - 1]) in constant time.
Usage:
  rmq = RMQ(values)
  rmq.query(inclusive, exclusive)
Time: O(|V| log |V| + Q)
Status: stress-tested
"""

from typing import List, TypeVar, Generic

T = TypeVar('T')

class RMQ(Generic[T]):
    def __init__(self, V: List[T]):
        self.jmp = [V[:]]
        pw = 1
        k = 1
        while pw * 2 <= len(V):
            new_row = []
            for j in range(len(V) - pw * 2 + 1):
                new_row.append(min(self.jmp[k - 1][j], self.jmp[k - 1][j + pw]))
            self.jmp.append(new_row)
            pw *= 2
            k += 1
    
    def query(self, a: int, b: int) -> T:
        assert a < b, "Invalid range query"
        dep = (b - a).bit_length() - 1
        return min(self.jmp[dep][a], self.jmp[dep][b - (1 << dep)])

