"""
Author: Chen Xing
Date: 2009-10-13
License: CC0
Description: Fast bipartite matching algorithm. Graph g should be a list
of neighbors of the left partition, and btoa should be a vector full of
-1's of the same size as the right partition. Returns the size of
the matching. btoa[i] will be the match for vertex i on the right side,
or -1 if it's not matched.
Usage: btoa = [-1] * m; hopcroft_karp(g, btoa)
Time: O(√V E)
Status: stress-tested by MinimumVertexCover, and tested on oldkattis.adkbipmatch and SPOJ:MATCHING
"""

from typing import List

def _dfs(a: int, L: int, g: List[List[int]], btoa: List[int], A: List[int], B: List[int]) -> bool:
    """DFS for Hopcroft-Karp"""
    if A[a] != L:
        return False
    A[a] = -1
    for b in g[a]:
        if B[b] == L + 1:
            B[b] = 0
            if btoa[b] == -1 or _dfs(btoa[b], L + 1, g, btoa, A, B):
                btoa[b] = a
                return True
    return False

def hopcroft_karp(g: List[List[int]], btoa: List[int]) -> int:
    """
    Fast bipartite matching using Hopcroft-Karp algorithm.
    g[i] = neighbors of node i in left partition
    btoa = matches for right partition (initially all -1)
    Returns size of matching
    """
    res = 0
    A = [0] * len(g)
    B = [0] * len(btoa)
    cur = []
    next_nodes = []
    
    while True:
        A = [0] * len(g)
        B = [0] * len(btoa)
        
        # Find starting nodes for BFS (layer 0)
        cur = []
        for a in btoa:
            if a != -1:
                A[a] = -1
        for a in range(len(g)):
            if A[a] == 0:
                cur.append(a)
        
        # Find all layers using BFS
        lay = 1
        while True:
            islast = False
            next_nodes = []
            for a in cur:
                for b in g[a]:
                    if btoa[b] == -1:
                        B[b] = lay
                        islast = True
                    elif btoa[b] != a and not B[b]:
                        B[b] = lay
                        next_nodes.append(btoa[b])
            
            if islast:
                break
            if not next_nodes:
                return res
            
            for a in next_nodes:
                A[a] = lay
            cur = next_nodes
            lay += 1
        
        # Use DFS to scan for augmenting paths
        for a in range(len(g)):
            res += _dfs(a, 0, g, btoa, A, B)

