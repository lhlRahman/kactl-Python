"""
Author: Lukas Polacek
Date: 2009-10-28
License: CC0
Source: Czech graph algorithms book, by Demel. (Tarjan's algorithm)
Description: Finds strongly connected components in a
directed graph. If vertices u, v belong to the same component,
we can reach u from v and vice versa.
Usage: scc(graph, callback) visits all components
in reverse topological order. comp[i] holds the component
index of a node (a component only has edges to components with
lower index). Returns (comp, ncomps).
Time: O(E + V)
Status: Bruteforce-tested for N <= 5
"""

from typing import List, Callable

class SCCState:
    def __init__(self, n: int):
        self.val = [0] * n
        self.comp = [-1] * n
        self.z = []
        self.cont = []
        self.Time = 0
        self.ncomps = 0

def _dfs(j: int, g: List[List[int]], f: Callable, state: SCCState) -> int:
    """DFS helper for SCC"""
    state.Time += 1
    low = state.val[j] = state.Time
    state.z.append(j)
    
    for e in g[j]:
        if state.comp[e] < 0:
            low = min(low, state.val[e] if state.val[e] else _dfs(e, g, f, state))
    
    if low == state.val[j]:
        while True:
            x = state.z.pop()
            state.comp[x] = state.ncomps
            state.cont.append(x)
            if x == j:
                break
        f(state.cont)
        state.cont = []
        state.ncomps += 1
    
    state.val[j] = low
    return low

def scc(g: List[List[int]], f: Callable):
    """Find strongly connected components"""
    n = len(g)
    state = SCCState(n)
    
    for i in range(n):
        if state.comp[i] < 0:
            _dfs(i, g, f, state)
    
    return state.comp, state.ncomps

