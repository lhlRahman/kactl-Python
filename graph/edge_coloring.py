"""
Author: Simon Lindholm
Date: 2020-10-12
License: CC0
Source: https://en.wikipedia.org/wiki/Misra_%26_Gries_edge_coloring_algorithm
Description: Given a simple, undirected graph with max degree D, computes a
(D + 1)-coloring of the edges such that no neighboring edges share a color.
(D-coloring is NP-hard, but can be done for bipartite graphs by repeated
matchings of max-degree nodes.)
Time: O(NM)
Status: stress-tested, tested on kattis:gamescheduling
"""

from typing import List, Tuple

def edge_coloring(N: int, edges: List[Tuple[int, int]]) -> List[int]:
    """
    Compute edge coloring with D+1 colors where D is max degree.
    N = number of nodes
    edges = list of (u, v) edges
    Returns list of colors for each edge
    """
    # Count degrees
    cc = [0] * (N + 1)
    for u, v in edges:
        cc[u] += 1
        cc[v] += 1
    
    ncols = max(cc) + 1
    ret = [0] * len(edges)
    
    # adj[u][c] = vertex adjacent to u with color c (or -1)
    adj = [[-1] * ncols for _ in range(N)]
    free = [0] * N  # free[u] = smallest free color at u
    
    fan = [0] * N
    cc_list = [0] * ncols
    loc = [0] * ncols
    
    for edge_idx, (u, v) in enumerate(edges):
        fan[0] = v
        for i in range(ncols):
            loc[i] = 0
        
        c = free[u]
        ind = 0
        
        # Build fan
        while True:
            d = free[v]
            if loc[d]:
                break
            if adj[u][d] == -1:
                break
            v = adj[u][d]
            ind += 1
            loc[d] = ind
            cc_list[ind] = d
            fan[ind] = v
        
        cc_list[loc[d]] = c
        
        # Invert path
        cd = d
        at = u
        end = u
        while at != -1:
            next_at = adj[at][cd]
            adj[at][cd], adj[end][cd ^ c ^ d] = adj[end][cd ^ c ^ d], adj[at][cd]
            end = at
            at = next_at
            cd ^= c ^ d
        
        # Rotate fan
        i = 0
        while adj[fan[i]][d] != -1:
            left = fan[i]
            i += 1
            right = fan[i]
            e = cc_list[i]
            adj[u][e] = left
            adj[left][e] = u
            adj[right][e] = -1
            free[right] = e
        
        adj[u][d] = fan[i]
        adj[fan[i]][d] = u
        
        # Update free colors
        for y in [fan[0], u, end]:
            free[y] = 0
            while adj[y][free[y]] != -1:
                free[y] += 1
    
    # Determine colors
    for i, (u, v) in enumerate(edges):
        ret[i] = 0
        while adj[u][ret[i]] != v:
            ret[i] += 1
    
    return ret

