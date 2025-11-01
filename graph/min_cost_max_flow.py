"""
Author: Stanford
Date: Unknown
Source: Stanford Notebook
Description: Min-cost max-flow.
If costs can be negative, call set_pi before maxflow, but note that negative cost cycles are not supported.
To obtain the actual flow, look at positive values only.
Status: Tested on kattis:mincostmaxflow, stress-tested against another implementation
Time: O(F E log(V)) where F is max flow. O(VE) for set_pi.
"""

import heapq
from typing import List, Tuple

INF = 10**18

class MinCostMaxFlow:
    class Edge:
        def __init__(self, from_node: int, to: int, rev: int, cap: int, cost: int):
            self.from_node = from_node
            self.to = to
            self.rev = rev
            self.cap = cap
            self.cost = cost
            self.flow = 0
    
    def __init__(self, N: int):
        self.N = N
        self.ed = [[] for _ in range(N)]
        self.seen = [False] * N
        self.dist = [INF] * N
        self.pi = [0] * N
        self.par = [None] * N
    
    def add_edge(self, from_node: int, to: int, cap: int, cost: int):
        """Add edge with capacity and cost"""
        if from_node == to:
            return
        self.ed[from_node].append(self.Edge(from_node, to, len(self.ed[to]), cap, cost))
        self.ed[to].append(self.Edge(to, from_node, len(self.ed[from_node]) - 1, 0, -cost))
    
    def path(self, s: int):
        """Find shortest path using Dijkstra with potentials"""
        self.seen = [False] * self.N
        self.dist = [INF] * self.N
        self.dist[s] = 0
        
        # Priority queue: (distance, node)
        pq = [(0, s)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if self.seen[u]:
                continue
            self.seen[u] = True
            di = self.dist[u] + self.pi[u]
            
            for e in self.ed[u]:
                if not self.seen[e.to]:
                    val = di - self.pi[e.to] + e.cost
                    if e.cap - e.flow > 0 and val < self.dist[e.to]:
                        self.dist[e.to] = val
                        self.par[e.to] = e
                        heapq.heappush(pq, (self.dist[e.to], e.to))
        
        for i in range(self.N):
            self.pi[i] = min(self.pi[i] + self.dist[i], INF)
    
    def maxflow(self, s: int, t: int) -> Tuple[int, int]:
        """Compute min-cost max-flow. Returns (flow, cost)"""
        totflow = 0
        totcost = 0
        
        while True:
            self.path(s)
            if not self.seen[t]:
                break
            
            # Find bottleneck
            fl = INF
            x = self.par[t]
            while x:
                fl = min(fl, x.cap - x.flow)
                x = self.par[x.from_node]
            
            totflow += fl
            
            # Update flow
            x = self.par[t]
            while x:
                x.flow += fl
                self.ed[x.to][x.rev].flow -= fl
                x = self.par[x.from_node]
        
        # Calculate cost
        for i in range(self.N):
            for e in self.ed[i]:
                totcost += e.cost * e.flow
        
        return (totflow, totcost // 2)
    
    def set_pi(self, s: int):
        """Initialize potentials for negative costs (Bellman-Ford)"""
        self.pi = [INF] * self.N
        self.pi[s] = 0
        
        for _ in range(self.N):
            changed = False
            for i in range(self.N):
                if self.pi[i] != INF:
                    for e in self.ed[i]:
                        if e.cap:
                            v = self.pi[i] + e.cost
                            if v < self.pi[e.to]:
                                self.pi[e.to] = v
                                changed = True
            if not changed:
                break
        else:
            raise AssertionError("Negative cost cycle detected")

