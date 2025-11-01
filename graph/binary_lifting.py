"""
Author: Johan Sannemo
Date: 2015-02-06
License: CC0
Source: Folklore
Description: Calculate power of two jumps in a tree,
to support fast upward jumps and LCAs.
Assumes the root node points to itself.
Time: construction O(N log N), queries O(log N)
Status: Tested at Petrozavodsk, also stress-tested via LCA.cpp
"""

from typing import List

def tree_jump(P: List[int]) -> List[List[int]]:
    """
    Build binary lifting table.
    P[i] = parent of node i (root points to itself)
    Returns jump table for fast ancestor queries
    """
    on = 1
    d = 1
    while on < len(P):
        on *= 2
        d += 1
    
    jmp = [P[:] for _ in range(d)]
    for i in range(1, d):
        for j in range(len(P)):
            jmp[i][j] = jmp[i - 1][jmp[i - 1][j]]
    
    return jmp

def jump(tbl: List[List[int]], nod: int, steps: int) -> int:
    """Jump 'steps' ancestors up from node 'nod'"""
    for i in range(len(tbl)):
        if steps & (1 << i):
            nod = tbl[i][nod]
    return nod

def lca(tbl: List[List[int]], depth: List[int], a: int, b: int) -> int:
    """Find lowest common ancestor of nodes a and b"""
    if depth[a] < depth[b]:
        a, b = b, a
    a = jump(tbl, a, depth[a] - depth[b])
    if a == b:
        return a
    for i in range(len(tbl) - 1, -1, -1):
        c = tbl[i][a]
        d = tbl[i][b]
        if c != d:
            a = c
            b = d
    return tbl[0][a]
