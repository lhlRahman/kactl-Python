"""
Author: Simon Lindholm
Date: 2015-02-24
License: CC0
Source: Wikipedia, tinyKACTL
Description: Push-relabel using the highest label selection rule and the gap heuristic. Quite fast in practice.
To obtain the actual flow, look at positive values only.
Time: O(V^2√E)
Status: Tested on Kattis and SPOJ, and stress-tested
"""

from typing import List

class PushRelabel:
    class Edge:
        def __init__(self, dest: int, back: int, c: int):
            self.dest = dest
            self.back = back
            self.f = 0
            self.c = c
    
    def __init__(self, n: int):
        self.g = [[] for _ in range(n)]
        self.ec = [0] * n
        self.cur = [0] * n
        self.hs = [[] for _ in range(2 * n)]
        self.H = [0] * n
    
    def add_edge(self, s: int, t: int, cap: int, rcap: int = 0):
        """Add edge with capacity and optional reverse capacity"""
        if s == t:
            return
        self.g[s].append(self.Edge(t, len(self.g[t]), cap))
        self.g[t].append(self.Edge(s, len(self.g[s]) - 1, rcap))
    
    def add_flow(self, e: Edge, f: int):
        """Push flow through edge"""
        back = self.g[e.dest][e.back]
        if not self.ec[e.dest] and f:
            self.hs[self.H[e.dest]].append(e.dest)
        e.f += f
        e.c -= f
        self.ec[e.dest] += f
        back.f -= f
        back.c += f
        self.ec[back.dest] -= f
    
    def calc(self, s: int, t: int) -> int:
        """Calculate max flow from s to t"""
        v = len(self.g)
        self.H[s] = v
        self.ec[t] = 1
        co = [0] * (2 * v)
        co[0] = v - 1
        
        for i in range(v):
            self.cur[i] = 0
        
        for e in self.g[s]:
            self.add_flow(e, e.c)
        
        hi = 0
        while True:
            # Find highest non-empty level
            while hi >= 0 and not self.hs[hi]:
                hi -= 1
            if hi < 0:
                return -self.ec[s]
            
            u = self.hs[hi].pop()
            
            # Discharge u
            while self.ec[u] > 0:
                if self.cur[u] == len(self.g[u]):
                    # Relabel
                    self.H[u] = 10**9
                    for e in self.g[u]:
                        if e.c and self.H[u] > self.H[e.dest] + 1:
                            self.H[u] = self.H[e.dest] + 1
                            self.cur[u] = self.g[u].index(e)
                    
                    co[self.H[u]] += 1
                    co[hi] -= 1
                    if co[hi] == 0 and hi < v:
                        for i in range(v):
                            if hi < self.H[i] < v:
                                co[self.H[i]] -= 1
                                self.H[i] = v + 1
                    hi = self.H[u]
                else:
                    e = self.g[u][self.cur[u]]
                    if e.c and self.H[u] == self.H[e.dest] + 1:
                        self.add_flow(e, min(self.ec[u], e.c))
                    else:
                        self.cur[u] += 1
    
    def left_of_min_cut(self, a: int) -> bool:
        """Check if node is on left side of min cut"""
        return self.H[a] >= len(self.g)

