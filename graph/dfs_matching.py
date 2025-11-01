"""
Author: Lukas Polacek
Date: 2009-10-28
License: CC0
Description: Simple bipartite matching algorithm. Graph g should be a list
of neighbors of the left partition, and btoa should be a vector full of
-1's of the same size as the right partition. Returns the size of
the matching. btoa[i] will be the match for vertex i on the right side,
or -1 if it's not matched.
Time: O(VE)
Usage: btoa = [-1] * m; dfs_matching(g, btoa)
Status: works
"""

from typing import List

def _find(j: int, g: List[List[int]], btoa: List[int], vis: List[bool]) -> bool:
    """DFS to find augmenting path"""
    if btoa[j] == -1:
        return True
    vis[j] = True
    di = btoa[j]
    for e in g[di]:
        if not vis[e] and _find(e, g, btoa, vis):
            btoa[e] = di
            return True
    return False

def dfs_matching(g: List[List[int]], btoa: List[int]) -> int:
    """
    Find maximum bipartite matching using DFS.
    g[i] = list of neighbors of node i in left partition
    btoa = list of matches for right partition (initially all -1)
    Returns size of matching
    """
    for i in range(len(g)):
        vis = [False] * len(btoa)
        for j in g[i]:
            if _find(j, g, btoa, vis):
                btoa[j] = i
                break
    
    return len(btoa) - btoa.count(-1)

