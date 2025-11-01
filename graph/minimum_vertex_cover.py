"""
Author: Johan Sannemo, Simon Lindholm
Date: 2016-12-15
License: CC0
Description: Finds a minimum vertex cover in a bipartite graph.
The size is the same as the size of a maximum matching, and
the complement is a maximum independent set.
Status: stress-tested
"""

from typing import List
from .dfs_matching import dfs_matching

def minimum_vertex_cover(g: List[List[int]], n: int, m: int) -> List[int]:
    """
    Find minimum vertex cover in bipartite graph.
    g = adjacency list for left partition (size n)
    m = size of right partition
    Returns list of vertices in the cover (left vertices as 0..n-1, right as n..n+m-1)
    """
    match = [-1] * m
    res = dfs_matching(g, match)
    
    lfound = [True] * n
    seen = [False] * m
    
    for it in match:
        if it != -1:
            lfound[it] = False
    
    q = [i for i in range(n) if lfound[i]]
    
    while q:
        i = q.pop()
        lfound[i] = True
        for e in g[i]:
            if not seen[e] and match[e] != -1:
                seen[e] = True
                q.append(match[e])
    
    cover = []
    for i in range(n):
        if not lfound[i]:
            cover.append(i)
    for i in range(m):
        if seen[i]:
            cover.append(n + i)
    
    assert len(cover) == res
    return cover

