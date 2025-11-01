"""
Author: chilli, pajenegod
Date: 2020-02-20
License: CC0
Source: Folklore
Description: Data structure for computing lowest common ancestors in a tree
(with 0 as root). C should be an adjacency list of the tree, either directed
or undirected.
Time: O(N log N + Q)
Status: stress-tested
"""

from typing import List
import sys
sys.path.append('..')
from data_structures.rmq import RMQ

class LCA:
    def __init__(self, C: List[List[int]]):
        self.T = 0
        self.time = [0] * len(C)
        self.path = []
        self.ret = []
        self.dfs(C, 0, -1)
        self.rmq = RMQ(self.ret)
    
    def dfs(self, C: List[List[int]], v: int, par: int):
        self.time[v] = self.T
        self.T += 1
        for y in C[v]:
            if y != par:
                self.path.append(v)
                self.ret.append(self.time[v])
                self.dfs(C, y, v)
    
    def lca(self, a: int, b: int) -> int:
        if a == b:
            return a
        ta = self.time[a]
        tb = self.time[b]
        if ta > tb:
            ta, tb = tb, ta
        return self.path[self.rmq.query(ta, tb)]

