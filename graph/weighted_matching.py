"""
Author: Benjamin Qi, chilli
Date: 2020-04-04
License: CC0
Source: https://github.com/bqi343/USACO/blob/master/Implementations/content/graphs%20(12)/Matching/Hungarian.h
Description: Given a weighted bipartite graph, matches every node on
the left with a node on the right such that no
nodes are in two matchings and the sum of the edge weights is minimal. Takes
cost[N][M], where cost[i][j] = cost for L[i] to be matched with R[j] and
returns (min cost, match), where L[i] is matched with
R[match[i]]. Negate costs for max cost. Requires N <= M.
Time: O(N^2 M)
Status: Tested on kattis:cordonbleu, stress-tested
"""

from typing import List, Tuple

def hungarian(a: List[List[int]]) -> Tuple[int, List[int]]:
    """
    Hungarian algorithm for minimum cost bipartite matching.
    a[i][j] = cost for L[i] to be matched with R[j]
    Returns (min_cost, match) where L[i] is matched with R[match[i]]
    """
    if not a:
        return (0, [])
    
    n = len(a) + 1
    m = len(a[0]) + 1
    u = [0] * n
    v = [0] * m
    p = [0] * m
    ans = [0] * (n - 1)
    
    for i in range(1, n):
        p[0] = i
        j0 = 0  # add "dummy" worker 0
        dist = [float('inf')] * m
        pre = [-1] * m
        done = [False] * (m + 1)
        
        while True:  # Dijkstra
            done[j0] = True
            i0 = p[j0]
            delta = float('inf')
            j1 = 0
            
            for j in range(1, m):
                if not done[j]:
                    cur = a[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < dist[j]:
                        dist[j] = cur
                        pre[j] = j0
                    if dist[j] < delta:
                        delta = dist[j]
                        j1 = j
            
            for j in range(m):
                if done[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    dist[j] -= delta
            
            j0 = j1
            if not p[j0]:
                break
        
        # Update alternating path
        while j0:
            j1 = pre[j0]
            p[j0] = p[j1]
            j0 = j1
    
    for j in range(1, m):
        if p[j]:
            ans[p[j] - 1] = j - 1
    
    return (-v[0], ans)  # min cost

