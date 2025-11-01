"""
Author: Simon Lindholm
Date: 2019-12-31
License: CC0
Source: folklore
Description: Eulerian undirected/directed path/cycle algorithm.
Input should be a list of (dest, global edge index), where
for undirected graphs, forward/backward edges have the same index.
Returns a list of nodes in the Eulerian path/cycle with src at both start and end, or
empty list if no cycle/path exists.
Time: O(V + E)
Status: stress-tested
"""

from typing import List, Tuple

def euler_walk(gr: List[List[Tuple[int, int]]], nedges: int, src: int = 0) -> List[int]:
    """
    Find Eulerian path/cycle in a graph.
    gr[i] = list of (destination, edge_index) pairs
    nedges = total number of edges
    src = starting node
    Returns list of nodes in Eulerian path, or empty list if none exists
    """
    n = len(gr)
    D = [0] * n
    its = [0] * n
    eu = [0] * nedges
    ret = []
    s = [src]
    
    D[src] += 1  # to allow Euler paths, not just cycles
    
    while s:
        x = s[-1]
        it = its[x]
        end = len(gr[x])
        
        if it == end:
            ret.append(x)
            s.pop()
            continue
        
        y, e = gr[x][it]
        its[x] += 1
        
        if not eu[e]:
            D[x] -= 1
            D[y] += 1
            eu[e] = 1
            s.append(y)
    
    # Check if valid Eulerian path/cycle
    for x in D:
        if x < 0 or len(ret) != nedges + 1:
            return []
    
    return ret[::-1]

