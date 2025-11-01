"""
Author: Chen Xing
Date: 2009-10-13
License: CC0
Source: N/A
Description: Flow algorithm with guaranteed complexity O(VE^2). To get edge flow values, compare
capacities before and after, and take the positive values only.
Status: stress-tested
"""

from typing import List, Dict

def edmonds_karp(graph: List[Dict[int, int]], source: int, sink: int) -> int:
    """
    Edmonds-Karp max flow algorithm.
    graph[i] is a dict mapping node j to capacity from i to j
    Returns maximum flow from source to sink
    """
    assert source != sink, "Source and sink must be different"
    
    flow = 0
    n = len(graph)
    par = [-1] * n
    q = [0] * n
    
    while True:
        # BFS to find augmenting path
        par = [-1] * n
        par[source] = source
        ptr = 1
        q[0] = source
        
        i = 0
        while i < ptr:
            x = q[i]
            for e_first, e_second in graph[x].items():
                if par[e_first] == -1 and e_second > 0:
                    par[e_first] = x
                    q[ptr] = e_first
                    ptr += 1
                    if e_first == sink:
                        break
            else:
                i += 1
                continue
            break
        
        # No augmenting path found
        if par[sink] == -1:
            return flow
        
        # Find minimum capacity along path
        inc = float('inf')
        y = sink
        while y != source:
            inc = min(inc, graph[par[y]][y])
            y = par[y]
        
        # Update flow
        flow += inc
        y = sink
        while y != source:
            p = par[y]
            graph[p][y] -= inc
            if graph[p][y] <= 0:
                del graph[p][y]
            if y not in graph:
                graph[y] = {}
            graph[y][p] = graph[y].get(p, 0) + inc
            y = p
    
    return flow

