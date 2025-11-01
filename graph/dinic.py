"""
Author: chilli
Date: 2019-04-26
License: CC0
Source: https://cp-algorithms.com/graph/dinic.html
Description: Flow algorithm with complexity O(VE log U) where U = max |cap|.
O(min(E^{1/2}, V^{2/3})E) if U = 1; O(√V E) for bipartite matching.
Status: Tested on SPOJ FASTFLOW and SPOJ MATCHING, stress-tested
"""

from typing import List

class Dinic:
    class Edge:
        def __init__(self, to: int, rev: int, c: int, oc: int):
            self.to = to
            self.rev = rev
            self.c = c
            self.oc = oc
        
        def flow(self) -> int:
            """Get current flow through this edge"""
            return max(self.oc - self.c, 0)
    
    def __init__(self, n: int):
        self.lvl = [0] * n
        self.ptr = [0] * n
        self.q = [0] * n
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, a: int, b: int, c: int, rcap: int = 0):
        """Add edge from a to b with capacity c and reverse capacity rcap"""
        self.adj[a].append(self.Edge(b, len(self.adj[b]), c, c))
        self.adj[b].append(self.Edge(a, len(self.adj[a]) - 1, rcap, rcap))
    
    def dfs(self, v: int, t: int, f: int) -> int:
        """DFS to push flow"""
        if v == t or f == 0:
            return f
        
        while self.ptr[v] < len(self.adj[v]):
            e = self.adj[v][self.ptr[v]]
            if self.lvl[e.to] == self.lvl[v] + 1:
                p = self.dfs(e.to, t, min(f, e.c))
                if p:
                    e.c -= p
                    self.adj[e.to][e.rev].c += p
                    return p
            self.ptr[v] += 1
        return 0
    
    def calc(self, s: int, t: int) -> int:
        """Calculate max flow from s to t"""
        flow = 0
        self.q[0] = s
        
        for L in range(31):
            while True:
                self.lvl = [0] * len(self.q)
                self.ptr = [0] * len(self.q)
                qi = 0
                qe = 1
                self.lvl[s] = 1
                
                # BFS to build level graph
                while qi < qe and not self.lvl[t]:
                    v = self.q[qi]
                    qi += 1
                    for e in self.adj[v]:
                        if not self.lvl[e.to] and (e.c >> (30 - L)):
                            self.q[qe] = e.to
                            qe += 1
                            self.lvl[e.to] = self.lvl[v] + 1
                
                # Push flow while path exists
                while True:
                    p = self.dfs(s, t, float('inf'))
                    if not p:
                        break
                    flow += p
                
                if not self.lvl[t]:
                    break
        
        return flow
    
    def left_of_min_cut(self, a: int) -> bool:
        """Check if node a is on the left side of min cut"""
        return self.lvl[a] != 0

