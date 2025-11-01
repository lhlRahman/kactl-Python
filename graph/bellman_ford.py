"""
Author: Simon Lindholm
Date: 2015-02-23
License: CC0
Source: http://en.wikipedia.org/wiki/Bellman-Ford_algorithm
Description: Calculates shortest paths from s in a graph that might have negative edge weights.
Unreachable nodes get dist = inf; nodes reachable through negative-weight cycles get dist = -inf.
Time: O(VE)
Status: Tested on kattis:shortestpath3
"""

from typing import List

INF = 10**18

class Edge:
    def __init__(self, a: int, b: int, w: int):
        self.a = a
        self.b = b
        self.w = w
    
    def s(self) -> int:
        return self.a if self.a < self.b else -self.a

class Node:
    def __init__(self):
        self.dist = INF
        self.prev = -1

def bellman_ford(nodes: List[Node], eds: List[Edge], s: int):
    """
    Find shortest paths from source s.
    nodes = list of Node objects (modified in-place)
    eds = list of Edge objects
    s = source node
    """
    nodes[s].dist = 0
    eds.sort(key=lambda ed: ed.s())
    
    lim = len(nodes) // 2 + 2
    
    for i in range(lim):
        for ed in eds:
            cur = nodes[ed.a]
            dest = nodes[ed.b]
            if abs(cur.dist) == INF:
                continue
            d = cur.dist + ed.w
            if d < dest.dist:
                dest.prev = ed.a
                dest.dist = d if i < lim - 1 else -INF
    
    # Propagate negative infinity
    for i in range(lim):
        for e in eds:
            if nodes[e.a].dist == -INF:
                nodes[e.b].dist = -INF
